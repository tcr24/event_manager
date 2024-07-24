import pytest
from pydantic import ValidationError
from app.schemas.user import UserCreate

def test_valid_usernames():
    valid_usernames = ['testuser', 'test-user', 'test_user', 'testuser123']
    for username in valid_usernames:
        user = UserCreate(email='test@example.com', password='testpass', nickname=username)
        assert user.nickname == username

def test_invalid_usernames():
    invalid_usernames = ['te', 'test user', 'test?user', 'user!']
    for username in invalid_usernames:
        with pytest.raises(ValidationError):
            UserCreate(email='test@example.com', password='testpass', nickname=username)
