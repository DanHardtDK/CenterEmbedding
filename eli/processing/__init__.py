def create_default_nshot_examples(examples: list[str]) -> str:
    raise NotImplementedError(
        "Not implemented yet - TODO: Do we need nshot examples for default?"
    )


def create_cot_nshot_examples(examples: list[str]) -> str:
    nshot_examples = "\n".join(
        [
            (
                f"Context: {e['Context']}\n"
                + f"A1: {e['A1']}\n"
                + f"A2: {e['A2']}\n"
                + f"A3: {e['A3']}\n"
                + f"Question: {e['Q']}\n"
                + f"Answer: {e['A']}\n"
            )
            for e in examples
        ]
    )
    if nshot_examples:
        return "Here are several examples with the correct outputs:\n" + nshot_examples
    return ""


def filter_nshot_examples(
    sampled_examples: list[str], tune_n: int, strategy: str
) -> (list[str], list[str]):
    if strategy == "default":
        output = (
            create_default_nshot_examples(
                sampled_examples[:tune_n]
            ),  # choose n-shot examples
            sampled_examples[tune_n:],  # remove n-shot examples from examples
        )
    else:
        output = (
            create_cot_nshot_examples(
                sampled_examples[:tune_n]
            ),  # choose n-shot examples
            sampled_examples[tune_n:],  # remove n-shot examples from examples
        )

    return output
