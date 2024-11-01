from typing import List, Optional
from pathlib import Path
from datetime import datetime
from configparser import ConfigParser
from argparse import ArgumentParser
from argparse_pydantic import add_args_from_model, create_model_obj
from pydantic import BaseModel, Field, model_validator, field_validator
from functools import cached_property

from utils.loggers import logger


class Args(BaseModel):
    """Command line arguments for the experiment"""

    file_list: Optional[str] = Field(
        default=None,
        description="Path for txt containing list of files to test against",
    )
    model: Optional[str] = Field(default=None, description="LLM to test")
    prompt_strategy: Optional[str] = Field(
        default=None,
        description="Chain-of-thought strategy to use for tuning",
        choices=[
            "default",
            "center_embed",
            "center_embed_tn1",
            "center_embed_tn2",
            "center_embed_tn2_2",
            "center_embed_tn3",
            "center_embed_tn3_2",
            "center_embed_tn3_only",            
            "center_embed_tn4",
            "center_embed_tn4_2",
            "center_embed_tn4_only",                                                
            "supervised_cot",
            "unsupervised_cot",
        ],
    )
    sample_n: int = Field(
        default=10, description="number of ellipses examples to test", gt=0, lt=10_000
    )
    iterations: int = Field(
        default=1,
        description="number of iterations to run",
        choices=[1, 2, 3, 5, 10, 50],
    )
    tuning_n: int = Field(
        default=0,
        description="Number of in-prompt n-shot examples to use for tuning",
        choices=[0, 1, 2, 3, 5, 10, 20],
    )
    seed: Optional[int] = Field(
        default=42, description="random seed for reproducibility"
    )

    # @field_validator("tuning_n", mode="before")
    # def warn_tuning_n(self):
    #     if self.tuning_n > 0:
    #         logger.warning(
    #             "Warning: Tuning is not yet implemented."
    #             "Setting tuning_n does absolutely nothing."
    #         )
    #     return self

    @model_validator(mode="after")
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

    @cached_property
    def files(self) -> List[str]:
        """Returns specific paths of json files containing examples
        to test against. Will have the format '<type>/<file>.json'
        where 'type' is the type of linguistic challenge in snake_case.
        (e.g. 'center_embed')"""
        file_path = Path(self.file_list)
        if not file_path.exists():
            raise FileNotFoundError(f"File {file_path.cwd()} does not exist")
        v = file_path.read_text().splitlines()
        for file in v:
            if not (Path("data") / file).exists():
                raise FileNotFoundError(f"File {file} does not exist")
            if not file.endswith(".json"):
                raise ValueError(f"File {file} must be a json file")
        return v

    @cached_property
    def EXP_NAME(self) -> str:
        """Returns a unique name for the experiment"""
        name = "_".join(
            [
                self.model,
                self.prompt_strategy,
                self.file_list.split("/")[-1],
                f"N{str(self.sample_n)}",
                f"Tn{str(self.tuning_n)}",
                f"I{str(self.iterations)}",
                f"{datetime.now().strftime('%d-%m-%y-%H-%M')}",
            ]
        )
        assert "/" not in name, "Name cannot contain '/'"
        return name


parser = add_args_from_model(ArgumentParser(), Args)
arguments = parser.parse_args()

ARGS = create_model_obj(Args, arguments)

####################
# CONFIG PARSER
# Read the config file
####################

CONFIG = ConfigParser()
CONFIG.read("config.cfg")
