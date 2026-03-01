"""File request models using Pydantic for input validation."""

from pydantic import BaseModel, Field


class FileRequest(BaseModel):
    """Request model for file generation."""

    filename: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Name of file without extension"
    )
    content: str = Field(
        ...,
        min_length=1,
        description="Content to include in the file"
    )
    metadata: dict | None = Field(
        None,
        description="Optional metadata for the file"
    )

    class Config:
        """Pydantic config."""

        str_strip_whitespace = True
