# tests/test_schemas/test_user_schemas.py

import pytest
from pydantic import ValidationError
from app.schemas.user import UserCreate

def test_valid_username():
    user = UserCreate(email="test@example.com", username="validuser")
    assert user.username == "validuser"

def test_invalid_username():
    with pytest.raises(ValidationError):
        UserCreate(email="test@example.com", username="invalid user")  # Space is invalid

def test_short_username():
    with pytest.raises(ValidationError):
        UserCreate(email="test@example.com", username="aa")  # Too short

def test_long_username():
    with pytest.raises(ValidationError):
        UserCreate(email="test@example.com", username="a" * 51)  # Too long
