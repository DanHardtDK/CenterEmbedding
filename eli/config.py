from configparser import ConfigParser
from datetime import datetime
import logging

from utils.loggers import logger
from utils.parsers import ARGS, EXAMPLE_FILES, SAVE_DIR, COT_STRATEGY  # noqa: F401


####################
# BEAUTIFY ARGS FOR LOGGING
####################

PRETTY_ARGS = ARGS.__dict__
PRETTY_ARGS["files"] = ARGS.files.name

####################
# CONFIG PARSER
####################

_config_parser = ConfigParser()
_config_parser.read("config.cfg")
if not _config_parser.get("DEFAULT", "API_KEY"):
    raise ValueError("API_KEY not set in config.cfg")

API_KEY = _config_parser.get("DEFAULT", "API_KEY")

if not _config_parser.get("DEFAULT", "LLAMA_KEY"):
    raise ValueError("LLAMA_KEY not set in config.cfg")

LLAMA_KEY = _config_parser.get("DEFAULT", "LLAMA_KEY")


####################
# Set MODEL
####################

MODEL = ARGS.model


if MODEL[:5] == 'llama':
    API_KEY = LLAMA_KEY

    
####################
# ADJUST SAMPLE SIZE
# add tune_n to sample size, since we
# will be using tune_n examples for tuning
####################

ARGS.sample_n += ARGS.tuning_n


####################
# SET RUN ID
####################

RUN_ID = (
    f"{ARGS.files}_"
    + f"{ARGS.sample_n}_"
    + f"{ARGS.model}_"
    + f"{datetime.now().strftime('%d%m%Y_%H%M%S')}"
).lstrip("data/lists/")


####################
# ADD FILE HANDLER TO LOGGER
####################


file_handler = logging.FileHandler(f"logs/{SAVE_DIR}/{RUN_ID}.log")  # updated on run
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter("%(message)s"))
logger.addHandler(file_handler)
