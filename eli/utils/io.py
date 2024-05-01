import json
from pathlib import Path


def load_files(FILES) -> list:
    """Load files from a list of paths."""

    for file in FILES:
        with file.open(encoding="UTF-8") as source:
            yield file, json.load(source)


def write_to_file(file, lines) -> None:
    """Write lines to a file."""

    with file.open(mode="a", encoding="UTF-8") as target:
        for line in lines:
            target.write(line + "\n")
        # target.writelines(lines)


def create_file(dir, name, init_text="") -> None:
    """Create a file and write lines to it."""

    path = Path(dir) / name
    path.touch(exist_ok=False)
    path.write_text(init_text)
    return path
    # target.writelines(lines
