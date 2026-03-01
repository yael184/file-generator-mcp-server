"""Plain text file generation service."""

from pathlib import Path
from models.file_request import FileRequest
from models.file_response import build_file_response
from services.file_service import get_output_path
from validation import validate_filename, validate_content


def generate_txt(request: FileRequest) -> dict:
    """
    Generate a plain text file from content.

    Args:
        request: FileRequest with filename and content

    Returns:
        Dictionary with file metadata and commands
    """
    validate_filename(request.filename)
    validate_content(request.content)

    output_path = get_output_path(request.filename, "txt")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(request.content)

    return build_file_response(output_path)
