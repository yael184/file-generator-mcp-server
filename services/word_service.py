"""Word (DOCX) file generation service."""

from pathlib import Path
from docx import Document
from models.file_request import FileRequest
from models.file_response import build_file_response
from services.file_service import get_output_path
from validation import validate_filename, validate_content


def generate_docx(request: FileRequest) -> dict:
    """
    Generate a Word document from text content.

    Args:
        request: FileRequest with filename and content

    Returns:
        Dictionary with file metadata and commands
    """
    validate_filename(request.filename)
    validate_content(request.content)

    output_path = get_output_path(request.filename, "docx")

    doc = Document()
    doc.add_paragraph(request.content)

    doc.save(str(output_path))

    return build_file_response(output_path)
