def test_update_profile_fields(db_session):
    user = create_user(db_session)
    user_update = UserUpdate(nickname='newnickname', bio='new bio', profile_picture_url='http://newpic.url')
    updated_user = update_user_profile(db_session, user, user_update)
    assert updated_user.nickname == 'newnickname'
    assert updated_user.bio == 'new bio'
    assert updated_user.profile_picture_url == 'http://newpic.url'
