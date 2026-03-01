"""vCard file generation service."""

from pathlib import Path
from vobject import vCard
from models.file_request import FileRequest
from models.file_response import build_file_response
from services.file_service import get_output_path
from validation import validate_filename, validate_content


def generate_vcard(request: FileRequest) -> dict:
    """
    Generate a vCard (VCF) file from content.

    Args:
        request: FileRequest with filename and content

    Returns:
        Dictionary with file metadata and commands
    """
    validate_filename(request.filename)
    validate_content(request.content)

    output_path = get_output_path(request.filename, "vcf")

    card = vCard()
    card.add("fn")
    card.fn.value = request.filename
    card.add("n")
    card.n.value = vCard.Name(family=request.filename)
    card.add("note")
    card.note.value = request.content

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(card.serialize())

    return build_file_response(output_path)
