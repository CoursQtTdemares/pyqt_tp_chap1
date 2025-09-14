from pathlib import Path


def load_styles(style_path: Path) -> str:
    if not style_path.exists():
        raise FileNotFoundError(f"Style file not found: {style_path}")

    if style_path.suffix != ".qss":
        raise ValueError(f"Style file must have a .qss extension: {style_path}")

    with open(style_path, "r") as file:
        return file.read()
