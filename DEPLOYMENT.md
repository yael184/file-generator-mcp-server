# File Generator MCP - Installation & Deployment Guide

## Quick Start (Windows)

```bash
# 1. Navigate to project directory
cd c:\Users\TZADY\Desktop\New folder\file-generator-mcp

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Start the MCP server
python main.py
```

## Quick Start (Linux/macOS)

```bash
# 1. Navigate to project directory
cd ~/path/to/file-generator-mcp

# 2. Create virtual environment
python3 -m venv venv

# 3. Activate virtual environment
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Start the MCP server
python main.py
```

## Project Files Created

### Core Application Files
- **main.py** - FastMCP server with 12 async tools registered
- **validation.py** - Input validation logic with security checks
- **requirements.txt** - All Python dependencies

### Models Layer (models/)
- **file_request.py** - Pydantic FileRequest model for input validation
- **file_response.py** - build_file_response() function for structured responses
- **metadata.py** - FileMetadata model for file information
- **__init__.py** - Package initialization

### Services Layer (services/)
- **file_service.py** - Reusable helpers: ensure_output_folder(), get_output_path()
- **pdf_service.py** - PDF file generation
- **word_service.py** - Word document (DOCX) generation
- **excel_service.py** - Excel spreadsheet (XLSX) generation
- **csv_service.py** - CSV file generation
- **json_service.py** - JSON file generation
- **txt_service.py** - Plain text file generation
- **html_service.py** - HTML file generation
- **markdown_service.py** - Markdown file generation
- **pptx_service.py** - PowerPoint presentation generation
- **image_service.py** - PNG image file generation
- **calendar_service.py** - iCalendar (ICS) event generation
- **vcard_service.py** - vCard (VCF) contact generation
- **__init__.py** - Package initialization

### Documentation & Testing
- **README.md** - Complete project documentation (see file for details)
- **tests.py** - Test suite with async PDF generation test
- **quick_test.py** - Quick verification test (auto-generated)

### Output Directory
- **output/** - Generated files stored here (auto-created)

## Architecture Overview

```
┌─────────────────────────────────────────────────────────┐
│                    FastMCP Server                        │
│                       (main.py)                          │
│                                                          │
│  12 Async Tools (using asyncio.to_thread)              │
│  ├─ create_pdf      ├─ create_csv       ├─ create_ics  │
│  ├─ create_docx     ├─ create_json      └─ create_vcard│
│  ├─ create_excel    ├─ create_txt                      │
│  ├─ create_html     ├─ create_markdown                 │
│  └─ create_pptx     └─ create_image                    │
│                                                          │
└────────────────┬────────────────────────────────────────┘
                 │
    ┌────────────┴────────────┐
    │                         │
┌───▼──────────────────┐ ┌──▼──────────────────┐
│   Models Layer       │ │  Validation Layer   │
│  (models/*)          │ │  (validation.py)    │
│                      │ │                     │
│ • FileRequest        │ │ • validate_filename │
│ • FileResponse       │ │ • validate_content  │
│ • FileMetadata       │ │ • get_safe_filename │
└──────┬───────────────┘ └─────────────────────┘
       │
       │ Pydantic validation
       │
┌──────▼──────────────────────────────────────┐
│        Services Layer (services/*)           │
│     12 Synchronous Service Functions        │
│                                              │
│ • pdf_service.generate_pdf()                │
│ • word_service.generate_docx()              │
│ • excel_service.generate_excel()            │
│ • csv_service.generate_csv()                │
│ • json_service.generate_json()              │
│ • txt_service.generate_txt()                │
│ • html_service.generate_html()              │
│ • markdown_service.generate_markdown()      │
│ • pptx_service.generate_pptx()              │
│ • image_service.generate_image()            │
│ • calendar_service.generate_ics()           │
│ • vcard_service.generate_vcard()            │
│                                              │
│ File Helpers (file_service.py):             │
│ • ensure_output_folder()                    │
│ • get_output_path()                         │
└──────┬───────────────────────────────────────┘
       │
       │ Generates files
       │
       ▼
    output/
    └─ *.pdf, *.docx, *.xlsx, *.csv, *.json, etc.
```

## Tool Response Format

All tools return JSON responses with this structure:

```json
{
    "success": true,
    "filename": "example.pdf",
    "path": "C:\\Users\\...\\output\\example.pdf",
    "uri": "file:///C:/Users/.../output/example.pdf",
    "download_command": "copy \"...\" \"%USERPROFILE%\\Downloads\\\"",
    "open_command": "start \"\" \"...\""
}
```

## Features

✅ **Clean Architecture** - Strict separation of concerns
✅ **Async Tools** - All MCP tools are async for concurrency
✅ **Sync Services** - Efficient synchronous file operations
✅ **Pydantic Validation** - Strong input validation
✅ **12 File Types** - PDF, Word, Excel, CSV, JSON, TXT, HTML, Markdown, PowerPoint, PNG, ICS, VCF
✅ **Cross-Platform** - OS-aware commands for Windows/Linux/Mac
✅ **Type Hints** - Full type annotations throughout
✅ **Error Handling** - Comprehensive validation and error messages
✅ **Production Ready** - No TODOs, complete implementations

## Dependencies

All packages installed from requirements.txt:
- mcp>=0.10.0 - Model Context Protocol
- pydantic>=2.0.0 - Data validation
- fpdf2>=2.7.0 - PDF generation
- python-docx>=0.8.11 - Word documents
- pandas>=2.0.0 - Data manipulation
- openpyxl>=3.0.0 - Excel support
- python-pptx>=0.6.21 - PowerPoint
- Pillow>=10.0.0 - Image processing
- icalendar>=5.0.0 - Calendar events
- vobject>=0.9.6.1 - vCard support

## Testing

The project includes tests.py with async test for PDF creation:

```bash
# Run tests with pytest
pytest tests.py -v

# Or directly
python tests.py
```

Quick verification test (auto-generated):

```bash
python quick_test.py
```

## Configuration

### Filename Validation Rules
- Maximum 100 characters
- Alphanumeric, underscore, dash, space only
- No path traversal (no `..`, `/`, `\\`)
- No Windows reserved names (CON, PRN, AUX, NUL, COM1, etc.)

### Content Validation
- Cannot be empty
- Automatically trimmed of whitespace

### Output Location
- All files saved to `project_root/output/` folder
- Auto-created if doesn't exist
- Each file gets absolute path, URI, and OS commands

## Troubleshooting

### Port Already in Use
The MCP server runs on a socket. If you get connection issues, ensure:
1. Previous process is terminated
2. No other MCP servers on the same connection

### Import Errors
Ensure virtual environment is activated:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### Missing Dependencies
Reinstall requirements:
```bash
pip install -r requirements.txt
```

## Extending the Project

To add a new file type:

1. Create `services/new_service.py`:
```python
def generate_format(request: FileRequest) -> dict:
    validate_filename(request.filename)
    validate_content(request.content)
    output_path = get_output_path(request.filename, "ext")
    # Generate file
    return build_file_response(output_path)
```

2. Add async tool in `main.py`:
```python
@mcp.tool(description="...")
async def create_format(filename: str, content: str) -> dict:
    req = FileRequest(filename=filename, content=content)
    result = await asyncio.to_thread(service.generate_format, req)
    return result
```

3. Update `requirements.txt` with new dependencies

4. Update `README.md` documentation

## Performance

- Async tool invocation: Non-blocking, concurrent
- Service execution: Threaded to not block async loop
- File I/O: Optimized with pathlib
- Memory: Efficient streaming for large files
- Validation: Fast Pydantic validation

## Security

✅ Input validation prevents injection attacks
✅ Filename sanitization prevents directory traversal
✅ No arbitrary code execution
✅ Safe file paths using pathlib
✅ Proper encoding handling (UTF-8)

## License

This project is provided as-is for use with the Model Context Protocol.

## Support

For issues:
1. Check README.md for detailed documentation
2. Review code comments and docstrings
3. Run tests.py to verify functionality
4. Examine output/ folder for generated files
