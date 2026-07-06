
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from typing import Optional

class CreateTask(BaseModel):
    title: str = Field(..., min_length=4, max_length=40)
    description: str = Field(min_length=10, max_length=200, default="*not_provided*")
    is_done: bool = Field(default=False)

class UpdateTask(BaseModel):
    title: Optional[str] = Field(None, min_length=4, max_length=40)
    description: Optional[str] = Field(None, min_length=10, max_length=200)
    is_done: Optional[bool] = Field(None)

class ResponseTask(BaseModel):
    id: int
    title: str
    description: str
    is_done: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
