# app/schemas/user.py

class UserUpdate(BaseModel):
    bio: Optional[str] = None
    profile_picture_url: Optional[str] = None

    @validator("profile_picture_url")
    def validate_profile_picture_url(cls, v):
        if v and not v.startswith(("http://", "https://")):
            raise ValueError("Profile picture URL must start with http:// or https://")
        return v
