"""Markdown file generation service."""

from pathlib import Path
from models.file_request import FileRequest
from models.file_response import build_file_response
from services.file_service import get_output_path
from validation import validate_filename, validate_content


def generate_markdown(request: FileRequest) -> dict:
    """
    Generate a Markdown file from content.

    Args:
        request: FileRequest with filename and content

    Returns:
        Dictionary with file metadata and commands
    """
    validate_filename(request.filename)
    validate_content(request.content)

    output_path = get_output_path(request.filename, "md")

    # Add title from filename
    markdown = f"# {request.filename}\n\n{request.content}"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(markdown)

    return build_file_response(output_path)
