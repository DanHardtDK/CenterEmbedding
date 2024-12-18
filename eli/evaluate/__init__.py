import weave
import editdistance

from evaluate.evaluator import Evaluator  # noqa: F401
from utils.loggers import logger


def postprocess(string):
    return string.strip().lower().removeprefix("answer:").strip()


@weave.op()
def eval_function(target: str, model_output: str) -> dict:
    """Evaluate the model output against the target. We
    consider the model output correct if it exactly matches
    the target or if the edit distance between the two
    strings is less than 2."""


    
    if not model_output:
        logger.info("Model output is empty")
        model_output = ""

    print("Previous Model", model_output)        
    model_output = postprocess(model_output)
    edit_distance = editdistance.eval(target, model_output)

    exact_match = target.lower() == model_output
    fuzzy_match = edit_distance < 2
    correct = exact_match | fuzzy_match

    print("eval_function", "Target", target, "Model", model_output, "correct", correct, "exact", exact_match)
    
    logger.info(f"{target=} | {model_output=} | {correct=}")
    return {
        "correct": correct,
        "edit_distance": edit_distance,
        "exact_match": exact_match,
    }
