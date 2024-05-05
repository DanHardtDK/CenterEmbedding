import weave

def postprocess(string):
    return string.strip().lower()

@weave.op()
def evaluator(target: str, model_output: str) -> dict:
    model_output = postprocess(model_output)
    return {'correct': target == model_output}