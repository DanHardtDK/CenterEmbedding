import weave
import editdistance

from eli.utils.loggers import logger

def postprocess(string):
    return string.strip().lower()

@weave.op()
def evaluator(target: str, model_output: str) -> dict:
    model_output = postprocess(model_output)
    correct = target == model_output

    logger.info(f"Target: {target} | Model: {model_output} | Correct: {correct}")
    return {
        'correct': correct,
        'edit_distance': editdistance.eval(target, model_output)
    }