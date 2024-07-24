# app/schemas/user.py

from pydantic import BaseModel, EmailStr, validator, constr

class UserCreate(BaseModel):
    email: EmailStr
    username: constr(min_length=3, max_length=50)

    @validator("username")
    def validate_username(cls, v):
        if not v.isalnum():
            raise ValueError("Username must be alphanumeric")
        return v
