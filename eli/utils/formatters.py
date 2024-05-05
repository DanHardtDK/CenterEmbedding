from typing import Any


def format_examples(objects : list[dict[str, Any]]) -> list:
    """Format examples for Weave"""
    
    examples = [
        {
            "id": i,
            "context": ex["Context"],
            "question": ex["Q"],
            "target": ex["A"]
        }
    for i, ex in enumerate(objects)]
    return examples
