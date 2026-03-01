"""Reusable file service helpers."""

from pathlib import Path


def ensure_output_folder() -> Path:
    """
    Ensure output directory exists and return its path.

    Returns:
        Path object for the output folder
    """
    output_path = Path(__file__).parent.parent / "output"
    output_path.mkdir(exist_ok=True)
    return output_path


def get_output_path(filename: str, extension: str) -> Path:
    """
    Get full output path for a file.

    Args:
        filename: Name without extension
        extension: File extension without dot (e.g. "pdf", "docx")

    Returns:
        Path object for the output file
    """
    output_folder = ensure_output_folder()
    # Ensure extension starts with a dot
    if not extension.startswith("."):
        extension = f".{extension}"
    return output_folder / f"{filename}{extension}"
