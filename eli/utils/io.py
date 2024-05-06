import json
from typing import Any
from pathlib import Path


def load_files(FILES) -> tuple[str, list[dict[str, Any]]]:
    """Load files from a list of paths."""

    for file_path in FILES:
        with Path(f"data/{file_path}").open("r", encoding="UTF-8") as source:
            objects = json.load(source)
        yield file_path, objects