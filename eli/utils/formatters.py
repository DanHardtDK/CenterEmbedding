from typing import Any


def format_examples(objects: list[dict[str, Any]]) -> list:
    """Format examples for Weave, since the format is
    different from the one used in the other datasets."""

    examples = [
        {
            "id": i,
            "context": ex["Context"],
            "question": ex["Q"],
            "target": ex["A"],
            "level": ex["level"],
        }
        for i, ex in enumerate(objects)
    ]
    return examples

def format_prompt(few_shot_examples, answerForm) -> str:
    """prompt with optional few shot examples"""
    
    START_INSTRUCTION = "You will be given an example consisting of a context and a question to answer. The answer should always be "

    ANSWER_FORM = """ "The N V the N", where N stands for a noun, and V stands for a verb."""
    if answerForm == "YN":
        ANSWER_FORM = """ a single word, "Yes" or "No", and nothing else."""
    INSTRUCTION = START_INSTRUCTION + ANSWER_FORM
    
    FEW_SHOT = "Here are some examples:\n"

    END_INSTRUCTION = """Now answer the question:

Context: {context}
Question: {question}
"""

    concatenated_examples = "\n"
    if len(few_shot_examples) > 0:
        INSTRUCTION += FEW_SHOT
        few_shot_example_strings = [
            "Context: "+ d["context"] + "\nQuestion: "+ d["question"] +"\nAnswer: " + d["target"] + "\n"
            for d in few_shot_examples]
        concatenated_examples = "\n".join(few_shot_example_strings)
        print(few_shot_example_strings)

    return (INSTRUCTION + concatenated_examples + END_INSTRUCTION)

