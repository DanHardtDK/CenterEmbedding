from configparser import ConfigParser
from datetime import datetime
import logging

from eli.utils.loggers import logger
from eli.utils.args import ARGS


####################
# CONFIG PARSER
####################
#TODO: Fix this mess

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

