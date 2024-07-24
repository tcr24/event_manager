# tests/test_schemas/test_user_schemas.py

def test_valid_password():
    user = UserCreate(email="test@example.com", username="validuser", password="Validpass1!")

def test_invalid_password_no_digit():
    with pytest.raises(ValidationError):
        UserCreate(email="test@example.com", username="validuser", password="NoDigit!")

def test_invalid_password_no_upper():
    with pytest.raises(ValidationError):
        UserCreate(email="test@example.com", username="validuser", password="noupper1!")

def test_invalid_password_no_lower():
    with pytest.raises(ValidationError):
        UserCreate(email="test@example.com", username="validuser", password="NOLOWER1!")

def test_invalid_password_no_special():
    with pytest.raises(ValidationError):
        UserCreate(email="test@example.com", username="validuser", password="NoSpecial1")
