from datetime import timedelta
from jose import jwt
from app.services.auth_service import create_access_token, verify_token
from app.config import SECRET_KEY, ALGORITHM

def test_create_access_token():
    data = {"sub": "testuser"}
    token = create_access_token(data, expires_delta=timedelta(minutes=30))
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    assert payload["sub"] == "testuser"

def test_verify_token():
    data = {"sub": "testuser"}
    token = create_access_token(data, expires_delta=timedelta(minutes=30))
    credentials_exception = Exception("Invalid credentials")
    token_data = verify_token(token, credentials_exception)
    assert token_data.username == "testuser"
