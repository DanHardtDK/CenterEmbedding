from pathlib import Path
from argparse import ArgumentParser, FileType
from argparse_pydantic import add_args_from_model, create_model_obj
from typing import List, Optional
from pydantic import BaseModel, Field, FilePath, validator, rootvalidator

from models import MODEL_REGISTRY


class Args(BaseModel):
    """ Command line arguments for the experiment """
    files: Optional[List[FilePath]] = Field(
        default=None,
        description="list of files containing ellipsis type to test"
    )
    model: Optional[str] = Field(
        default=None,
        description="LLM to test"
    )
    cot: Optional[str] = Field(
        default=None, 
        description="Chain-of-thought strategy to use for tuning", 
        choices=["default", "centerembed", "supervised", "unsupervised"]
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

    @validator('model')
    def validate_model(cls, v):
        if v not in MODEL_REGISTRY:
            raise ValueError("Invalid model specified.")
        return v
    
    @validator('files', pre=True)
    def load_data_sources(cls, v):
        if v is not None:
            file_path = Path(v)
            v = file_path.read_text().splitlines()
        return v

    @root_validator
    def check_sample_greater_than_tuning(cls, values):
        sample_n = values.get('sample_n')
        tuning_n = values.get('tuning_n')
        if sample_n <= tuning_n + 1:
            raise ValueError("sample_n must be larger than tuning_n")

        ####################
        # ADJUST SAMPLE SIZE
        # add tune_n to sample size, since we
        # will be using tune_n examples for tuning
        ####################

        values["sample_n"] += tuning_n
        return values


    @property
    def LOAD_DIR(self) -> str:

        root_path = "data/"
        match self.cot:
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
                self.cot,
                str(self.sample_n),
                str(self.tuning_n),
            ]
        )
    

parser = argparse.ArgumentParser(prog="ellipses-experiment")
arguments = add_args_from_model(parser, Args).parse_args()

ARGS = create_model_obj(AppCfg, arguments)
