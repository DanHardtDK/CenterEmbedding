
import pdb  # noqa: F401
import random

import eli.utils.secrets as secrets
from eli.utils.args import ARGS
import utils.io as io
from utils.loggers import logger
from eli.models import MODEL_REGISTRY


####################
# CONFIG
####################
random.seed(ARGS.seed)

####################
# RUN EXPERIMENT
####################


def run() -> None:

    model = MODEL_REGISTRY[ARGS.model](ARGS.model)
    
    logger.info(
        f"STARTING EXPERIMENT '{c.RUN_ID}' {'='*10}\n\n"
        + f"{c.PRETTY_ARGS}\n"
        + f"SYSTEM PROMPT: {API.template.template}\n\n"
    )

    for iteration in range(c.ARGS.iterations):
        logger.info(
            f"{'=' * 30}\n" + f"STARTING ITER {iteration} / {c.ARGS.iterations}"
        )

        count_files = len(c.EXAMPLE_FILES) - 1
        for i, (examples_file, examples) in enumerate(io.load_files(c.EXAMPLE_FILES)):
            logger.info(
                f"{examples_file.name=} | "
                + f"EXAMPLES: {len(examples)} | "
                + f"PICKING {c.ARGS.sample_n - c.ARGS.tuning_n} W/ SEED {c.ARGS.seed}\n"
            )

            # RESET COUNTERS
            count_correct = 0

            ################
            # SAMPLE EXAMPLES
            ################
            examples: list = random.sample(examples, c.ARGS.sample_n)
            # if c.ARGS.tuning_n > 0:
            #     # TODO: Consider if we even need this
            #     _, examples = proc.filter_nshot_examples(examples, c.ARGS.tuning_n)
            # RUN THROUGH EXAMPLES
            for ex_count, example in enumerate(examples):
                logger.info(
                    f"Iter {iteration} | "
                    + f" DATASET {i}/{count_files} ({examples_file.name}) | "
                    + f"# EX {ex_count}\n{'='*30}\n"
                )

                ################
                # RUN QUERY
                ################

                correct_result: bool = API.query(
                    true_answer=example["A"],
                    context=example["Context"],
                    question=example["Q"],
                    examples=" ",
                )

                ################
                # UPDATE COUNT CORRECT
                ################

                count_correct += int(correct_result)

            ################
            # WRITE TO RESULTS LOG
            ################

            result_log = (
                f"{examples_file},"
                + f"{iteration},"
                + f"{ex_count+ 1},"
                + f"{count_correct},"  # +1 since ex_countstarts at 0
                + f"{count_correct / (ex_count+ 1)},"
            )
            logger.info(result_log)
            io.write_to_file(results_file, lines=[result_log])


if __name__ == "__main__":
    run()
