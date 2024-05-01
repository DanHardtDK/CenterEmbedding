from argparse import ArgumentParser, FileType
from pathlib import Path

from models import MODEL_REGISTRY


####################
# ARGUMENT PARSING
####################

arg_parser = ArgumentParser()
arg_parser.add_argument(
    "--files",
    "-f",
    help="list of files containing ellipsis type to test",
    type=FileType("r"),
)
models = arg_parser.add_argument(
    "--model",
    "-m",
    help="LLM to test",
    choices=list(MODEL_REGISTRY.keys()),
    type=str,
)
arg_parser.add_argument(
    "--cot",
    "-s",
    help="Chain-of-thought strategy to use for tuning",
    type=str,
    choices=[
        "default",
        "centerembed",
        "centerembedP1",
        "centerembedP2",
        "supervised",
        "unsupervised",
    ],
)
arg_parser.add_argument(
    "--sample_n",
    "-n",
    help="number of ellipses examples to test",
    type=int,
)
arg_parser.add_argument(
    "--iterations",
    "-i",
    help="number of iterations to run",
    type=int,
    choices=[1, 2, 3, 5, 10, 50],
    default=1,
)
arg_parser.add_argument(
    "--tuning_n",
    "-tn",
    help="Number of in-prompt n-shot examples to use for tuning",
    type=int,
    choices=[0, 1, 2, 3, 5, 10, 20],
    default=0,
)
arg_parser.add_argument(
    "--seed",
    "-sd",
    help="random seed for reproducibility",
    type=int,
)

ARGS = arg_parser.parse_args()

####################
# SET STRATEGY AND IO DIRS
####################

COT_STRATEGY = ARGS.cot
SAVE_DIR = (
    f"ellipses-{('CoT-' + COT_STRATEGY) if COT_STRATEGY != 'default' else COT_STRATEGY}"
)
if (
    COT_STRATEGY == "centerembed"
    or COT_STRATEGY == "centerembedP1"
    or COT_STRATEGY == "centerembedP2"
):
    SAVE_DIR = "centerEmbed"

LOAD_DIR = f"data/ellipses{'-CoT' if COT_STRATEGY != 'default' else ''}"
if (
    COT_STRATEGY == "centerembed"
    or COT_STRATEGY == "centerembedP1"
    or COT_STRATEGY == "centerembedP2"
):
    LOAD_DIR = "data/centerEmbed"

####################
# FILTER & VALIDATE ARGS
####################

# check that files is not empty
files = ARGS.files.readlines()
data_files = Path(LOAD_DIR).glob("*.json")
EXAMPLE_FILES = [p for p in data_files if p.name in [f.strip("\n") for f in files]]

if not files:
    raise ValueError("files parameters is empty")

if len(EXAMPLE_FILES) != len(files):
    import pdb

    pdb.set_trace()
    raise ValueError("files contains invalid/missing file(s)")

if ARGS.sample_n <= ARGS.tuning_n + 1:
    raise ValueError("sample must be greater than tune_n")
