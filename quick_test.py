"""Quick test to verify the file generation system works."""

import logging
from services.txt_service import generate_txt
from models.file_request import FileRequest

# Configure logging for the quick test (no direct prints)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("file-generator.quick_test")

# Test text file generation
req = FileRequest(filename="test_output", content="Hello World - Test Content")
result = generate_txt(req)

logger.info("%s", "=" * 50)
logger.info("Text Service Test Successful")
logger.info("%s", "=" * 50)
logger.info("Success: %s", result["success"])
logger.info("Filename: %s", result["filename"])
logger.info("Path: %s", result["path"])
logger.info("URI: %s", result["uri"])
logger.info("Download Command: %s", result["download_command"])
logger.info("Open Command: %s", result["open_command"])
logger.info("%s", "=" * 50)
