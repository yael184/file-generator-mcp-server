"""PDF file generation service."""

from pathlib import Path
from fpdf import FPDF
from models.file_request import FileRequest
from models.file_response import build_file_response
from services.file_service import get_output_path
from validation import validate_filename, validate_content


def generate_pdf(request: FileRequest) -> dict:
    """
    Generate a PDF file from text content.

    Args:
        request: FileRequest with filename and content

    Returns:
        Dictionary with file metadata and commands
    """
    validate_filename(request.filename)
    validate_content(request.content)

    output_path = get_output_path(request.filename, "pdf")

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=12)

    # Handle multi-line content
    pdf.multi_cell(0, 10, request.content)

    pdf.output(str(output_path))

    return build_file_response(output_path)
