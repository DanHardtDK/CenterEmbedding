import pdb  # noqa: F401
import random
import asyncio

from utils.args import ARGS
from utils import io
from utils.loggers import logger  # noqa: F401
from utils.formatters import format_examples, format_prompt
from models import MODEL_REGISTRY
from templates import PROMPT_TEMPLATE_REGISTRY
from evaluate import Evaluator, eval_function


def run() -> None:
    # set seed
    random.seed(ARGS.seed)

    answerForm = "DEFAULT"
    if (ARGS.answerForm == "YN"):
        answerForm = "YN"
        
    # Load files
    files = io.load_files(ARGS.files)
    for examples_file, examples in files:
        # Format examples
        formatted_examples = format_examples(examples)

        # Sample examples
        sample_size = ARGS.sample_n + ARGS.tuning_n
        sampled_examples: list = random.sample(formatted_examples, sample_size)
        # tuning_examples = sampled_examples[:ARGS.tuning_n]
        # test_examples = sampled_examples[ARGS.tuning_n:]

        tuning_examples = random.sample(sampled_examples, ARGS.tuning_n)
        test_examples = [ex for ex in sampled_examples if ex not in tuning_examples]

        # Initialize Weave model object from
        # the model registry and the prompt template
        model = MODEL_REGISTRY[ARGS.model](
            model_name=ARGS.model,
            prompt_template=format_prompt(tuning_examples, answerForm)
                                    )
        
        # Initialize evaluation
        evaluator = Evaluator(
            name=f"{examples_file}-{ARGS.EXP_NAME}",
            description=f"Evaluation of '{ARGS.model}' on '{examples_file}' dataset.",
            dataset=test_examples,
            scorers=[eval_function],
            trials=1,
        )

        # Run evaluation
        # asyncio messes up order of predictions vs examples
        # changes workers from 3 to 1 so it is not async
        summary, predictions = asyncio.run(
            evaluator.evaluate(model=model, return_rows=True, workers=1)
        )

        io.write_results(
            summary=summary,
            predictions=predictions,
            examples_file=examples_file,
            parameters=ARGS,
            examples=test_examples,
        )


if __name__ == "__main__":
    run()
