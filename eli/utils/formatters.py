from typing import Any


def format_examples(objects : list[dict[str, Any]], example_file : str) -> list:
    """Format examples for Weave, since the format is
    different from the one used in the other datasets."""
    
    examples = [
        {
            "id": i,
            "context": ex["Context"],
            "question": ex["Q"],
            "target": ex["A"],
            "level": ex["level"],
            "example_file": example_file,
        }
    for i, ex in enumerate(objects)]
    return examples
