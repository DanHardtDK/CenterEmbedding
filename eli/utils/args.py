from pathlib import Path
from argparse import ArgumentParser, FileType
from argparse_pydantic import add_args_from_model, create_model_obj
from typing import List, Optional
from pydantic import BaseModel, Field, FilePath, field_validator, model_validator

from models import MODEL_REGISTRY


class Args(BaseModel):
    """ Command line arguments for the experiment """
    files: Optional[str] = Field(
        default=None, 
        description="Path for list of files containing ellipsis types to test"
    )
    model: Optional[str] = Field(
        default=None,
        description="LLM to test"
    )
    prompt_strategy: Optional[str] = Field(
        default=None, 
        description="Chain-of-thought strategy to use for tuning", 
        choices=["default", "centerembed", "supervised-cot", "unsupervised-cot"]
    )
    sample_n: int = Field(
        default=10, 
        description="number of ellipses examples to test",
        gt=0,
        lt=10_000
    )
    iterations: int = Field(
        default=1, 
        description="number of iterations to run", 
        choices=[1, 2, 3, 5, 10, 50]
    )
    tuning_n: int = Field(
        default=0,
        description="Number of in-prompt n-shot examples to use for tuning", 
        choices=[0, 1, 2, 3, 5, 10, 20]
    )
    seed: Optional[int] = Field(
        default=42,
        description="random seed for reproducibility"
    )

    @field_validator('model')
    @classmethod
    def validate_model(cls, v):
        if v not in MODEL_REGISTRY:
            raise ValueError("Invalid model specified.")
        return v
    
    @field_validator('files')
    @classmethod
    def load_data_sources(cls, v):
        file_path = Path(v)
        v = file_path.read_text().splitlines()
        return v

    @model_validator(mode='after')
    def check_sample_greater_than_tuning(self):
        sample_n = self.sample_n
        tuning_n = self.tuning_n
        if sample_n <= tuning_n + 1:
            raise ValueError("sample_n must be larger than tuning_n")

        ####################
        # ADJUST SAMPLE SIZE
        # add tune_n to sample size, since we
        # will be using tune_n examples for tuning
        ####################

        self.sample_n += tuning_n
        return self


    @property
    def LOAD_DIR(self) -> str:

        root_path = "data/"
        match self.prompt_strategy:
            case "centerembed", "centerembedP1", "centerembedP2":
                path = root_path + "centerEmbed"
            case "default":
                raise NotImplementedError("Default strategy not implemented")
            case "supervised":
                raise NotImplementedError("Supervised strategy not implemented")
            case "unsupervised":
                raise NotImplementedError("Unsupervised strategy not implemented")
            case _:
                raise ValueError("Invalid strategy specified")
        return path

    @property
    def EXP_NAME(self) -> str:
        return "_".join(
            [
                self.model,
                self.prompt_strategy,
                str(self.sample_n),
                str(self.tuning_n),
            ]
        )
    

parser = ArgumentParser(prog="ellipses-experiment")
parser = add_args_from_model(parser, Args)
arguments = parser.parse_args()

ARGS = create_model_obj(Args, arguments)


####################
# CONFIG PARSER
####################
#TODO: Fix this mess

from configparser import ConfigParser
from datetime import datetime
import logging

from utils.loggers import logger
from utils.args import ARGS

_config_parser = ConfigParser()
_config_parser.read("config.cfg")
if not _config_parser.get("DEFAULT", "API_KEY"):
    raise ValueError("API_KEY not set in config.cfg")

API_KEY = _config_parser.get("DEFAULT", "API_KEY")

if not _config_parser.get("DEFAULT", "LLAMA_KEY"):
    raise ValueError("LLAMA_KEY not set in config.cfg")

LLAMA_KEY = _config_parser.get("DEFAULT", "LLAMA_KEY")
if ARGS.model[:5] == 'llama':
    API_KEY = LLAMA_KEY

