# tests/test_schemas/test_user_schemas.py

def test_update_profile_fields():
    user_update = UserUpdate(bio="New bio", profile_picture_url="http://example.com/pic.jpg")
    assert user_update.bio == "New bio"
    assert user_update.profile_picture_url == "http://example.com/pic.jpg"

def test_update_profile_fields_invalid_url():
    with pytest.raises(ValidationError):
        UserUpdate(profile_picture_url="invalid_url")
