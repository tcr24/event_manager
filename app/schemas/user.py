from pydantic import BaseModel, EmailStr, validator
from typing import Optional
import re

class UserBase(BaseModel):
    email: EmailStr
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    nickname: Optional[str] = None
    bio: Optional[str] = None
    profile_picture_url: Optional[str] = None

    @validator('nickname')
    def validate_nickname(cls, v):
        if not v:
            return v
        if not re.match(r'^[\w-]{3,50}$', v):
            raise ValueError('Nickname must be 3-50 characters long and contain only letters, numbers, underscores, or hyphens.')
        return v

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    password: Optional[str] = None
