# File Generator MCP Server

A production-ready MCP (Model Context Protocol) server for generating various file types using FastMCP. This server provides async tools for creating PDF, Word, Excel, CSV, JSON, text, HTML, Markdown, PowerPoint, images, calendar events, and contact cards.

## Features

- **Async Tools**: All MCP tools are async for concurrent execution
- **Sync Services**: Services use efficient synchronous operations
- **Input Validation**: Pydantic models validate all inputs
- **Structured Responses**: Each tool returns metadata including file paths, URIs, and OS-specific commands
- **File Management**: Automatic output folder creation and file handling
- **Production Ready**: Full type hints, error handling, and separation of concerns
- **Cross-Platform**: OS-aware commands for file download and opening

## Supported File Types

- **PDF** - Text to PDF documents
- **DOCX** - Word documents
- **XLSX** - Excel spreadsheets
- **CSV** - Comma-separated values
- **JSON** - JSON formatted data
- **TXT** - Plain text files
- **HTML** - Web pages with styling
- **MD** - Markdown documents
- **PPTX** - PowerPoint presentations
- **PNG** - Images with text
- **ICS** - Calendar events
- **VCF** - Contact cards (vCard)

## Installation

### Prerequisites
- Python 3.14 or higher
- pip package manager

### Windows

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the server
python main.py
```

### Linux/macOS

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the server
python main.py
```

## Project Structure

```
file-generator-mcp/
├── main.py                      # FastMCP server with all tool definitions
├── requirements.txt             # Python dependencies
├── tests.py                     # Test suite
├── validation.py                # Input validation logic
├── models/
│   ├── file_request.py          # FileRequest Pydantic model
│   ├── file_response.py         # Response builder function
│   └── metadata.py              # Metadata model
├── services/
│   ├── file_service.py          # File operation helpers
│   ├── pdf_service.py           # PDF generation
│   ├── word_service.py          # Word document generation
│   ├── excel_service.py         # Excel spreadsheet generation
│   ├── csv_service.py           # CSV file generation
│   ├── json_service.py          # JSON file generation
│   ├── txt_service.py           # Text file generation
│   ├── html_service.py          # HTML file generation
│   ├── markdown_service.py      # Markdown file generation
│   ├── pptx_service.py          # PowerPoint generation
│   ├── image_service.py         # Image file generation
│   ├── calendar_service.py      # Calendar event (ICS) generation
│   └── vcard_service.py         # Contact card (VCF) generation
├── output/                      # Generated files (auto-created)
└── README.md                    # This file
```

## Architecture

### Clean Separation of Concerns

1. **Service Layer** (`services/`): Synchronous functions handling file generation
2. **Tool Layer** (`main.py`): Async MCP tools wrapping services via `asyncio.to_thread()`
3. **Model Layer** (`models/`): Pydantic models for validation and structured responses
4. **Validation Layer** (`validation.py`): Input validation rules

### Tool Pattern

Each tool follows this pattern:

```python
@mcp.tool(description="...")
async def create_format(filename: str, content: str) -> dict:
    req = FileRequest(filename=filename, content=content)
    result = await asyncio.to_thread(service.generate_format, req)
    return result
```

### Response Structure

All tools return responses in this structure:

```json
{
    "success": true,
    "filename": "example.pdf",
    "path": "/absolute/path/to/example.pdf",
    "uri": "file:///absolute/path/to/example.pdf",
    "download_command": "copy \"...\" \"%USERPROFILE%\\Downloads\\\"",
    "open_command": "start \"\" \"...\""
}
```

## Usage Examples

### Creating a PDF

```python
# Request
{
    "filename": "my_document",
    "content": "This is the PDF content"
}

# Response
{
    "success": true,
    "filename": "my_document.pdf",
    "path": "c:\\Users\\Username\\Desktop\\file-generator-mcp\\output\\my_document.pdf",
    "uri": "file:///c:/Users/Username/Desktop/file-generator-mcp/output/my_document.pdf",
    "download_command": "copy \"...\" \"%USERPROFILE%\\Downloads\\\"",
    "open_command": "start \"\" \"...\""
}
```

### Creating an Excel File

```python
# Request
{
    "filename": "data_table",
    "content": "Name\tAge\nJohn\t30\nJane\t28"
}

# Response includes same metadata structure
```

## Input Validation Rules

### Filename
- Not empty
- Max 100 characters
- Alphanumeric, underscore, dash, and space only
- No path traversal (no `..`, `/`, `\\`)
- No Windows reserved names (CON, PRN, AUX, NUL, etc.)

### Content
- Not empty

## File Output

All generated files are saved to the `output/` folder in the project directory. The server provides:
- Absolute file path
- File URI (file://)
- OS-specific download command (copy to Downloads folder)
- OS-specific open command (open the file)

## Testing

Run the test suite:

```bash
# With pytest
pytest tests.py -v

# Or directly with Python
python tests.py
```

## Error Handling

The server includes comprehensive error handling:
- Invalid filename validation with specific error messages
- Empty content validation
- Safe file path construction
- OS-aware command generation

## Requirements

See `requirements.txt` for all dependencies:

- **mcp** >= 0.10.0 - Model Context Protocol framework
- **pydantic** >= 2.0.0 - Data validation
- **fpdf2** >= 2.7.0 - PDF generation
- **python-docx** >= 0.8.11 - Word documents
- **pandas** >= 2.0.0 - Data manipulation
- **openpyxl** >= 3.10.0 - Excel support
- **python-pptx** >= 0.6.21 - PowerPoint presentations
- **Pillow** >= 10.0.0 - Image processing
- **icalendar** >= 5.0.0 - Calendar events
- **vobject** >= 0.9.6.1 - vCard support

## Code Quality

- ✅ Async tools with proper concurrency
- ✅ Synchronous services for I/O operations
- ✅ Full type hints throughout
- ✅ Pydantic validation models
- ✅ Production-ready implementation
- ✅ Pathlib for cross-platform paths
- ✅ Proper separation of concerns
- ✅ Error handling and validation

## Development

To extend the server with new file types:

1. Create a service in `services/new_service.py`
2. Implement `generate_format(request: FileRequest) -> dict`
3. Add a corresponding async tool in `main.py`
4. Add the new dependency to `requirements.txt`
5. Update this README with the new format

## License

This project is provided as-is for use with the Model Context Protocol.

## Support

For issues or questions, refer to the code structure and docstrings for detailed information about each component.
