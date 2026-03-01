"""File response models and builders."""

import os
from pathlib import Path


def build_file_response(file_path: Path) -> dict:
    """
    Build a structured file response with metadata.

    Args:
        file_path: Path object of the generated file

    Returns:
        Dict containing file metadata and OS-specific commands
    """
    absolute_path = str(file_path.resolve())
    filename = file_path.name
    file_uri = file_path.resolve().as_uri()

    # Detect OS and build appropriate commands
    if os.name == "nt":  # Windows
        download_command = f'copy "{absolute_path}" "%USERPROFILE%\\Downloads\\"'
        open_command = f'start "" "{absolute_path}"'
    else:  # Linux/Mac
        download_command = f'cp "{absolute_path}" ~/Downloads/'
        open_command = f'open "{absolute_path}"'

    return {
        "success": True,
        "filename": filename,
        "path": absolute_path,
        "uri": file_uri,
        "download_command": download_command,
        "open_command": open_command,
    }
