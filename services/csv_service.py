"""CSV file generation service."""

from pathlib import Path
import csv
from models.file_request import FileRequest
from models.file_response import build_file_response
from services.file_service import get_output_path
from validation import validate_filename, validate_content


def generate_csv(request: FileRequest) -> dict:
    """
    Generate a CSV file from content.

    Args:
        request: FileRequest with filename and content

    Returns:
        Dictionary with file metadata and commands
    """
    validate_filename(request.filename)
    validate_content(request.content)

    output_path = get_output_path(request.filename, "csv")

    lines = request.content.split("\n")

    with open(output_path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        for line in lines:
            if "," in line:
                writer.writerow(line.split(","))
            else:
                writer.writerow([line])

    return build_file_response(output_path)
