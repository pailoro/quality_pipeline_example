from services import service_two


def test_user_structure():
    """
    Test the structure of a user.
    """
    users = service_two.get_users()
    user = users[0]
    assert "id" in user
    assert "name" in user
    assert "username" in user
    assert "email" in user
