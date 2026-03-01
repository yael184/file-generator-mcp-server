"""Tests for file generator MCP server."""

import asyncio
import pytest
from pathlib import Path
from models.file_request import FileRequest
from services import pdf_service
from models.file_response import build_file_response


@pytest.mark.asyncio
async def test_create_pdf() -> None:
    """Test PDF file creation."""
    req = FileRequest(filename="test_document", content="This is a test PDF content.")
    result = await asyncio.to_thread(pdf_service.generate_pdf, req)

    assert result["success"] is True
    assert result["filename"] == "test_document.pdf"
    assert "path" in result
    assert "uri" in result
    assert "download_command" in result
    assert "open_command" in result

    # Verify file exists
    file_path = Path(result["path"])
    assert file_path.exists()

    # Clean up
    file_path.unlink()


def test_file_response_build() -> None:
    """Test file response builder."""
    test_path = Path(__file__).parent / "output" / "test.txt"
    test_path.parent.mkdir(exist_ok=True)
    test_path.write_text("test content")

    response = build_file_response(test_path)

    assert response["success"] is True
    assert response["filename"] == "test.txt"
    assert "path" in response
    assert "uri" in response
    assert "download_command" in response
    assert "open_command" in response

    # Clean up
    test_path.unlink()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
