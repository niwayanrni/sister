from pydantic import BaseModel, Field, field_validator
from typing import Dict, Any
from datetime import datetime
import uuid

class Event(BaseModel):
    topic: str
    event_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    source: str
    payload: Dict[str, Any]

    @field_validator("topic")
    def validate_topic(cls, v):
        if not v.strip():
            raise ValueError("Topic cannot be empty")
        return v
