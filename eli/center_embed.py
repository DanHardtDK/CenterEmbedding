
import pdb  # noqa: F401
import random
import weave
from weave import Evaluation
import asyncio

from utils.args import ARGS
from utils.io import load_files
from utils.loggers import logger
from utils.formatters import format_examples
from models import MODEL_REGISTRY
from evaluate import evaluator
from templates import PROMPT_TEMPLATE_REGISTRY


def run() -> None:

    random.seed(ARGS.seed)
    model = MODEL_REGISTRY[ARGS.model](
        model_name = ARGS.model,
        prompt_template = PROMPT_TEMPLATE_REGISTRY[ARGS.prompt_strategy]
    )

    weave.init(ARGS.EXP_NAME) # Initialize weave

    # Load files
    files = load_files(ARGS.files)
    for i, (examples_file, examples) in enumerate(files):

        # Format examples
        examples = format_examples(examples, examples_file)

        # Sample examples
        examples: list = random.sample(examples, ARGS.sample_n)

        # Initialize evaluation
        evaluation = weave.Evaluation(
            dataset=examples,
            scorers=[evaluator],
            trials=ARGS.iterations
        )

        # Run evaluation
        asyncio.run(evaluation.evaluate(model))
        

if __name__ == "__main__":
    run()
