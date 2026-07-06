
from datetime import datetime
from pydantic import BaseModel, ConfigDict, EmailStr, Field
from typing import Optional

class CreateUser(BaseModel):
    email: EmailStr = Field(..., min_length=10, max_length=254)
    username: str = Field(..., min_length=4, max_length=24)
    password: str = Field(..., min_length=8, max_length=64)

class UpdateUser(BaseModel):
    email: Optional[EmailStr] = Field(None, min_length=10, max_length=254)
    username: Optional[str] = Field(None, min_length=4, max_length=24)
    password: Optional[str] = Field(None, min_length=8, max_length=64)

class ResponseUser(BaseModel):
    id: int
    email: EmailStr
    username: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LoginUser(BaseModel):
    username: str = Field(..., min_length=4, max_length=24)
    password: str = Field(..., min_length=8, max_length=64)
