"""Image file generation service."""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from models.file_request import FileRequest
from models.file_response import build_file_response
from services.file_service import get_output_path
from validation import validate_filename, validate_content


def generate_image(request: FileRequest) -> dict:
    """
    Generate a PNG image with text content.

    Args:
        request: FileRequest with filename and content

    Returns:
        Dictionary with file metadata and commands
    """
    validate_filename(request.filename)
    validate_content(request.content)

    output_path = get_output_path(request.filename, "png")

    # Create image with white background
    img = Image.new("RGB", (800, 600), color="white")
    draw = ImageDraw.Draw(img)

    # Try to use a default font, fall back to default if not available
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except OSError:
        font = ImageFont.load_default()

    # Wrap text and draw on image
    lines = request.content.split("\n")
    y_position = 50

    for line in lines:
        draw.text((50, y_position), line, fill="black", font=font)
        y_position += 30

    img.save(str(output_path))

    return build_file_response(output_path)
