"""JSON file generation service."""

from pathlib import Path
import json
from models.file_request import FileRequest
from models.file_response import build_file_response
from services.file_service import get_output_path
from validation import validate_filename, validate_content


def generate_json(request: FileRequest) -> dict:
    """
    Generate a JSON file from content.

    Args:
        request: FileRequest with filename and content

    Returns:
        Dictionary with file metadata and commands
    """
    validate_filename(request.filename)
    validate_content(request.content)

    output_path = get_output_path(request.filename, "json")

    # Try to parse as JSON, otherwise wrap as simple object
    try:
        data = json.loads(request.content)
    except json.JSONDecodeError:
        data = {"content": request.content}

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    return build_file_response(output_path)
