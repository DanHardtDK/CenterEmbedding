import pdb  # noqa: F401
import random
import weave
import asyncio

from utils.args import ARGS
from utils import io
from utils.formatters import format_examples
from models import MODEL_REGISTRY
from templates import PROMPT_TEMPLATE_REGISTRY
from evaluate import Evaluator, eval_function


def run() -> None:
    # set seed
    random.seed(ARGS.seed)

    # Initialize Weave model object from
    # the model registry and the prompt template
    model = MODEL_REGISTRY[ARGS.model](
        model_name=ARGS.model,
        prompt_template=PROMPT_TEMPLATE_REGISTRY[ARGS.prompt_strategy],
    )

    weave.init(ARGS.EXP_NAME)  # Initialize weave experiment

    # Load files
    files = io.load_files(ARGS.files)
    for examples_file, examples in files:
        # Format examples
        examples = format_examples(examples)

        # Sample examples
        examples: list = random.sample(examples, ARGS.sample_n)

        # Initialize evaluation
        evaluator = Evaluator(
            name=f"{examples_file}-{ARGS.EXP_NAME}",
            description=f"Evaluation of '{ARGS.model}' on '{examples_file}' dataset.",
            dataset=examples,
            scorers=[eval_function],
            trials=ARGS.iterations,
        )

        # Run evaluation
        summary, predictions = asyncio.run(evaluator.evaluate(model, return_rows=True))

        io.write_results(
            summary=summary,
            predictions=predictions,
            examples_file=examples_file,
            parameters=ARGS,
            examples=examples,
        )


if __name__ == "__main__":
    run()
