"""Calendar (ICS) file generation service."""

from pathlib import Path
from datetime import datetime, timedelta
from icalendar import Calendar, Event
from models.file_request import FileRequest
from models.file_response import build_file_response
from services.file_service import get_output_path
from validation import validate_filename, validate_content


def generate_ics(request: FileRequest) -> dict:
    """
    Generate an iCalendar (ICS) file from content.

    Args:
        request: FileRequest with filename and content

    Returns:
        Dictionary with file metadata and commands
    """
    validate_filename(request.filename)
    validate_content(request.content)

    output_path = get_output_path(request.filename, "ics")

    cal = Calendar()
    cal.add("prodid", f"-//File Generator MCP//{request.filename}//EN")
    cal.add("version", "2.0")
    cal.add("calscale", "GREGORIAN")

    event = Event()
    event.add("summary", request.filename)
    event.add("description", request.content)
    event.add("dtstart", datetime.now())
    event.add("dtend", datetime.now() + timedelta(hours=1))
    event.add("dtstamp", datetime.now())
    event.add("uid", f"{request.filename}@file-generator-mcp")

    cal.add_component(event)

    with open(output_path, "wb") as f:
        f.write(cal.to_ical())

    return build_file_response(output_path)
