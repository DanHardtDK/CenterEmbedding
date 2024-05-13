import json
from typing import Any, Generator
from pathlib import Path


SUMMARY_COLUMNS = [
    "model",
    "prompt_strategy",
    "file_list",
    "example_file",
    "sample_n",
    "tuning_n",
    "iterations",
    "seed",
    "correct_true_count",
    "correct_true_fraction",
    "exact_match_true_count",
    "exact_match_true_fraction",
    "edit_distance_mean",
    "model_latency_mean",
]

PREDICTION_COLUMNS = [
    "id",
    "examples_file" "level",
    "context",
    "question",
    "target",
    "model_output",
    "correct",
    "edit_distance",
    "exact_match",
    "model_latency",
]


def load_files(FILES) -> Generator[tuple[str, list[dict[str, Any]]], None, None]:
    """Load files from a list of paths."""

    for file_path in FILES:
        with Path(f"data/{file_path}").open("r", encoding="UTF-8") as source:
            objects = json.load(source)
        yield file_path, objects


def make_file(EXP_NAME: str) -> Path:
    """Initialize the output directory and
    adds a summary file if it does not exist
    with the necessary columns."""

    exp_dir = Path(f"results/{EXP_NAME}")
    if not exp_dir.exists():
        # create the directory if it does not exist
        exp_dir.mkdir(parents=True, exist_ok=True)

        # create the summary file
        with (exp_dir / "summary.dat").open("a") as f:
            f.write(f"{','.join(SUMMARY_COLUMNS)}\n")

        # create the predictions file
        with (exp_dir / "predictions.dat").open("a") as f:
            f.write(f"{','.join(PREDICTION_COLUMNS)}\n")

    return exp_dir


def write_summary(
    file_path: Path, parameters: object, summary: dict, examples_file: Path
) -> None:
    summary_row = [
        parameters.model,
        parameters.prompt_strategy,
        parameters.sample_n,
        parameters.tuning_n,
        parameters.iterations,
        parameters.seed,
        parameters.file_list.split("/")[-1],
        examples_file.split("/")[-1],
        summary["eval_function"]["correct"]["true_count"],
        summary["eval_function"]["correct"]["true_fraction"],
        summary["eval_function"]["exact_match"]["true_count"],
        summary["eval_function"]["exact_match"]["true_fraction"],
        summary["eval_function"]["edit_distance"]["mean"],
        summary["model_latency"]["mean"],
    ]

    with (file_path / "summary.dat").open("a") as f:
        f.write(f"{','.join(map(str, summary_row))}\n")


def write_rows(
    file_path: Path, predictions: list, examples: list, examples_file: Path
) -> None:
    with (file_path / "predictions.dat").open("a") as f:
        for output, example in zip(predictions, examples):
            prediction_row = [
                example["id"],
                examples_file.split("/")[-1],
                example["level"],
                example["context"],
                example["question"],
                example["target"],
                output["model_output"],
                output["scores"]["eval_function"]["correct"],
                output["scores"]["eval_function"]["edit_distance"],
                output["scores"]["eval_function"]["exact_match"],
                output["model_latency"],
            ]
            f.write(f"{','.join(map(str, prediction_row))}\n")


def write_results(
    parameters: object,
    summary: dict,
    predictions: list,
    examples: list,
    examples_file: Path,
) -> None:
    """write results to files.

    1. Summary is appended to a .csv file, named "summary.csv", with the following format:
        model, prompt_strategy, file_list, example_file, sample_n, tuning_n, iterations, mean_score, mean_edit_distance, mean_latency
    2. Rows are written to a .dat file, named "predictions.dat" with the following format:
        model_output, scores, example_id
    3. Arguments are written to a .json file."""

    file_path = make_file(parameters.EXP_NAME)

    write_summary(file_path, parameters, summary, examples_file)
    write_rows(file_path, predictions, examples, examples_file)
