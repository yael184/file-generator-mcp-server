"""Metadata models for files."""

from datetime import datetime
from pydantic import BaseModel


class FileMetadata(BaseModel):
    """Metadata information about generated files."""

    filename: str
    path: str
    uri: str
    created_at: datetime
    size_bytes: int
    file_type: str

    class Config:
        """Pydantic config."""

        json_encoders = {datetime: lambda v: v.isoformat()}
