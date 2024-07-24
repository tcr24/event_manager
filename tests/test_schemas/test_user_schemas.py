def test_valid_passwords():
    valid_passwords = ['Password1!', 'Secure#1234', 'Complex@Password123']
    for password in valid_passwords:
        user = UserCreate(email='test@example.com', password=password, nickname='testuser')
        assert user.password == password

def test_invalid_passwords():
    invalid_passwords = ['short', 'nocapital1!', 'NOLOWER1!', 'NoNumber!', 'NoSpecial1']
    for password in invalid_passwords:
        with pytest.raises(ValidationError):
            UserCreate(email='test@example.com', password=password, nickname='testuser')
