"""FastMCP server for file generation with async tools and sync services.

This file now prints import errors to stderr to make debugging easier when the
Python environment used by the MCP host doesn't have the `mcp` package.
"""

import sys
import asyncio
import logging

logger = logging.getLogger("file-generator")
try:
    from mcp.server.fastmcp import FastMCP
except Exception:
    # Use logging (writes to stderr) rather than print to avoid breaking MCP
    logger.exception("Error importing FastMCP. Ensure 'mcp' is installed in the Python environment the MCP host is launching (e.g. .venv).")
    raise

from services import (
    pdf_service,
    word_service,
    excel_service,
    csv_service,
    json_service,
    txt_service,
    html_service,
    markdown_service,
    pptx_service,
    image_service,
    calendar_service,
    vcard_service,
)
from models.file_request import FileRequest


# Initialize FastMCP server
mcp = FastMCP("file-generator")


@mcp.tool(description="""
Create a PDF file from text content.

Use when:
- The user wants to save text as a PDF document
- The user needs a downloadable file
- The user wants a persistent file output

Inputs:
- filename: name of file without extension
- content: text content to include in the file

Returns:
- success: true if created
- filename: generated filename
- path: absolute file path
- uri: file:// URI
- download_command: OS command to copy file to Downloads
- open_command: OS command to open file
""")
async def create_pdf(filename: str, content: str) -> dict:
    """Create a PDF file from text content."""
    req = FileRequest(filename=filename, content=content)
    result = await asyncio.to_thread(pdf_service.generate_pdf, req)
    return result


@mcp.tool(description="""
Create a Word document from text content.

Use when:
- The user wants to save text as a Word document
- The user needs a .docx file
- The user wants editable document format

Inputs:
- filename: name of file without extension
- content: text content to include in the document

Returns:
- success: true if created
- filename: generated filename
- path: absolute file path
- uri: file:// URI
- download_command: OS command to copy file to Downloads
- open_command: OS command to open file
""")
async def create_docx(filename: str, content: str) -> dict:
    """Create a Word document from text content."""
    req = FileRequest(filename=filename, content=content)
    result = await asyncio.to_thread(word_service.generate_docx, req)
    return result


@mcp.tool(description="""
Create an Excel spreadsheet from text content.

Use when:
- The user wants to save data as an Excel file
- The user has tabular data (rows and columns)
- Lines are separated by newlines, columns by tabs or commas

Inputs:
- filename: name of file without extension
- content: text content with rows separated by newlines

Returns:
- success: true if created
- filename: generated filename
- path: absolute file path
- uri: file:// URI
- download_command: OS command to copy file to Downloads
- open_command: OS command to open file
""")
async def create_excel(filename: str, content: str) -> dict:
    """Create an Excel spreadsheet from text content."""
    req = FileRequest(filename=filename, content=content)
    result = await asyncio.to_thread(excel_service.generate_excel, req)
    return result


@mcp.tool(description="""
Create a CSV file from text content.

Use when:
- The user wants to save data as CSV format
- The user has comma-separated or tab-separated values
- The user needs a lightweight spreadsheet format

Inputs:
- filename: name of file without extension
- content: text content with rows separated by newlines

Returns:
- success: true if created
- filename: generated filename
- path: absolute file path
- uri: file:// URI
- download_command: OS command to copy file to Downloads
- open_command: OS command to open file
""")
async def create_csv(filename: str, content: str) -> dict:
    """Create a CSV file from text content."""
    req = FileRequest(filename=filename, content=content)
    result = await asyncio.to_thread(csv_service.generate_csv, req)
    return result


@mcp.tool(description="""
Create a JSON file from content.

Use when:
- The user wants to save data as JSON format
- The user has JSON-formatted content
- The content is not valid JSON, it will be wrapped in a simple object

Inputs:
- filename: name of file without extension
- content: text or JSON content

Returns:
- success: true if created
- filename: generated filename
- path: absolute file path
- uri: file:// URI
- download_command: OS command to copy file to Downloads
- open_command: OS command to open file
""")
async def create_json(filename: str, content: str) -> dict:
    """Create a JSON file from content."""
    req = FileRequest(filename=filename, content=content)
    result = await asyncio.to_thread(json_service.generate_json, req)
    return result


@mcp.tool(description="""
Create a plain text file from content.

Use when:
- The user wants to save text as a .txt file
- The user needs a simple text format
- The user wants universal file compatibility

Inputs:
- filename: name of file without extension
- content: text content

Returns:
- success: true if created
- filename: generated filename
- path: absolute file path
- uri: file:// URI
- download_command: OS command to copy file to Downloads
- open_command: OS command to open file
""")
async def create_txt(filename: str, content: str) -> dict:
    """Create a plain text file from content."""
    req = FileRequest(filename=filename, content=content)
    result = await asyncio.to_thread(txt_service.generate_txt, req)
    return result


@mcp.tool(description="""
Create an HTML file from text content.

Use when:
- The user wants to save text as an HTML web page
- The user wants to view content in a browser
- The user needs styled web content

Inputs:
- filename: name of file without extension
- content: text content to display

Returns:
- success: true if created
- filename: generated filename
- path: absolute file path
- uri: file:// URI
- download_command: OS command to copy file to Downloads
- open_command: OS command to open file
""")
async def create_html(filename: str, content: str) -> dict:
    """Create an HTML file from text content."""
    req = FileRequest(filename=filename, content=content)
    result = await asyncio.to_thread(html_service.generate_html, req)
    return result


@mcp.tool(description="""
Create a Markdown file from content.

Use when:
- The user wants to save text as a Markdown document
- The user wants a format compatible with GitHub/documentation
- The user needs structured text with formatting support

Inputs:
- filename: name of file without extension
- content: text content in markdown format

Returns:
- success: true if created
- filename: generated filename
- path: absolute file path
- uri: file:// URI
- download_command: OS command to copy file to Downloads
- open_command: OS command to open file
""")
async def create_markdown(filename: str, content: str) -> dict:
    """Create a Markdown file from content."""
    req = FileRequest(filename=filename, content=content)
    result = await asyncio.to_thread(markdown_service.generate_markdown, req)
    return result


@mcp.tool(description="""
Create a PowerPoint presentation from content.

Use when:
- The user wants to create a presentation
- The user needs a .pptx file
- The user wants slides with title and content

Inputs:
- filename: name of file without extension
- content: content for the presentation slides

Returns:
- success: true if created
- filename: generated filename
- path: absolute file path
- uri: file:// URI
- download_command: OS command to copy file to Downloads
- open_command: OS command to open file
""")
async def create_pptx(filename: str, content: str) -> dict:
    """Create a PowerPoint presentation from content."""
    req = FileRequest(filename=filename, content=content)
    result = await asyncio.to_thread(pptx_service.generate_pptx, req)
    return result


@mcp.tool(description="""
Create an image file with text content.

Use when:
- The user wants to save text as an image (PNG)
- The user wants to embed text in an image
- The user needs visual representation of text

Inputs:
- filename: name of file without extension
- content: text content to render on the image

Returns:
- success: true if created
- filename: generated filename
- path: absolute file path
- uri: file:// URI
- download_command: OS command to copy file to Downloads
- open_command: OS command to open file
""")
async def create_image(filename: str, content: str) -> dict:
    """Create an image file with text content."""
    req = FileRequest(filename=filename, content=content)
    result = await asyncio.to_thread(image_service.generate_image, req)
    return result


@mcp.tool(description="""
Create an iCalendar (ICS) file for calendar applications.

Use when:
- The user wants to create a calendar event
- The user needs an .ics file for importing to calendar apps
- The user wants iCalendar format

Inputs:
- filename: name of file without extension
- content: description of the calendar event

Returns:
- success: true if created
- filename: generated filename
- path: absolute file path
- uri: file:// URI
- download_command: OS command to copy file to Downloads
- open_command: OS command to open file
""")
async def create_ics(filename: str, content: str) -> dict:
    """Create an iCalendar file."""
    req = FileRequest(filename=filename, content=content)
    result = await asyncio.to_thread(calendar_service.generate_ics, req)
    return result


@mcp.tool(description="""
Create a vCard (VCF) file for contact information.

Use when:
- The user wants to create a contact card
- The user needs a .vcf file for contact management
- The user wants vCard format

Inputs:
- filename: name of file without extension (used as contact name)
- content: additional notes or information for the contact

Returns:
- success: true if created
- filename: generated filename
- path: absolute file path
- uri: file:// URI
- download_command: OS command to copy file to Downloads
- open_command: OS command to open file
""")
async def create_vcard(filename: str, content: str) -> dict:
    """Create a vCard file for contact information."""
    req = FileRequest(filename=filename, content=content)
    result = await asyncio.to_thread(vcard_service.generate_vcard, req)
    return result


if __name__ == "__main__":
    mcp.run()