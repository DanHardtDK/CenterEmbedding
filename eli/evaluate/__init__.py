import weave
import editdistance

from evaluate.evaluator import Evaluator  # noqa: F401
from utils.loggers import logger


def postprocess(string):
    return string.strip().lower().strip("answer:").strip()


@weave.op()
def eval_function(target: str, model_output: str) -> dict:
    """Evaluate the model output against the target. We
    consider the model output correct if it exactly matches
    the target or if the edit distance between the two
    strings is less than 2."""


    if model_output is None:
        model_output = ""
        return
    
    model_output = postprocess(model_output)
    edit_distance = editdistance.eval(target, model_output)

    exact_match = target == model_output
    fuzzy_match = edit_distance < 2
    correct = exact_match | fuzzy_match

    logger.info(f"{target=} | {model_output=} | {correct=}")
    return {
        "correct": correct,
        "edit_distance": edit_distance,
        "exact_match": exact_match,
    }
