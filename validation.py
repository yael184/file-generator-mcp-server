"""Validation logic for file operations."""

import re
from pathlib import Path


def validate_filename(filename: str) -> None:
    """
    Validate filename against security and format rules.

    Args:
        filename: The filename to validate

    Raises:
        ValueError: If filename is invalid

    Rules:
        - Not empty
        - Max 100 characters
        - Alphanumeric, underscore, dash only
        - No path traversal
        - No slashes or dots
    """
    if not filename or not filename.strip():
        raise ValueError("Filename cannot be empty")

    if len(filename) > 100:
        raise ValueError("Filename cannot exceed 100 characters")

    if "/" in filename or "\\" in filename:
        raise ValueError("Filename cannot contain slashes")

    if ".." in filename:
        raise ValueError("Path traversal not allowed")

    # Allow alphanumeric, underscore, dash, space (space gets replaced with underscore)
    if not re.match(r"^[a-zA-Z0-9_\s\-]+$", filename):
        raise ValueError(
            "Filename must contain only alphanumeric characters, underscores, dashes, and spaces"
        )

    # Avoid reserved words (Windows)
    reserved = {"con", "prn", "aux", "nul", "com1", "com2", "lpt1", "lpt2"}
    if filename.lower() in reserved:
        raise ValueError(f"Filename '{filename}' is reserved and cannot be used")


def validate_content(content: str) -> None:
    """
    Validate content is not empty.

    Args:
        content: The content to validate

    Raises:
        ValueError: If content is invalid
    """
    if not content or not content.strip():
        raise ValueError("Content cannot be empty")


def get_safe_filename(filename: str) -> str:
    """
    Clean and normalize filename.

    Args:
        filename: Original filename

    Returns:
        Safe filename with spaces replaced by underscores
    """
    validate_filename(filename)
    return filename.strip().replace(" ", "_")
