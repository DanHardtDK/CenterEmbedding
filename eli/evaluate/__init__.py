import weave

# Define any custom scoring function
@weave.op()
def evaluator(expected: dict, model_output: dict) -> dict:
    # Here is where you'd define the logic to score the model output
    return {'match': expected == model_output['generated_text']}
