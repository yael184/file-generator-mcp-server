"""Excel file generation service."""

from pathlib import Path
import pandas as pd
from models.file_request import FileRequest
from models.file_response import build_file_response
from services.file_service import get_output_path
from validation import validate_filename, validate_content


def generate_excel(request: FileRequest) -> dict:
    """
    Generate an Excel spreadsheet from content.

    Args:
        request: FileRequest with filename and content

    Returns:
        Dictionary with file metadata and commands
    """
    validate_filename(request.filename)
    validate_content(request.content)

    output_path = get_output_path(request.filename, "xlsx")

    # Split content by newlines for rows, by tabs/commas for columns
    lines = request.content.split("\n")
    data = []

    for line in lines:
        if "\t" in line:
            row = line.split("\t")
        elif "," in line:
            row = line.split(",")
        else:
            row = [line]
        data.append(row)

    df = pd.DataFrame(data)
    df.to_excel(str(output_path), index=False, header=False)

    return build_file_response(output_path)
