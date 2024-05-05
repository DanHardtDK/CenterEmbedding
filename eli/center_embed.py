
import pdb  # noqa: F401
import random
import weave
from weave import Evaluation
import asyncio

from utils.args import ARGS, API_KEY
from utils.io import load_files
from utils.loggers import logger
from utils.formatters import format_examples
from models import MODEL_REGISTRY
from evaluate import evaluator
from templates.prompts import CE_TEMPLATE



def run() -> None:

    random.seed(ARGS.seed)
    model = MODEL_REGISTRY[ARGS.model](
        model_name = ARGS.model,
        api_key = API_KEY, # TODO: Make dynamic
        prompt_template = CE_TEMPLATE # TODO: Make dynamic, support for few-shot
    )

    weave.init(ARGS.EXP_NAME) # Initialize weave

    files = load_files(ARGS.files)
    for i, (examples_file, examples) in enumerate(files):
        examples = format_examples(examples)

        ################
        # SAMPLE EXAMPLES
        ################

        examples: list = random.sample(examples, ARGS.sample_n)

        ################
        # RUN EVALUATION
        ################

        evaluation = weave.Evaluation(
            dataset=examples,
            scorers=[evaluator],
            trials=ARGS.iterations
        )

        asyncio.run(evaluation.evaluate(model))



if __name__ == "__main__":
    run()
