from services import service_two


def test_get_users():
    """
    Test the get_users function t.
    """
    users = service_two.get_users()
    assert isinstance(users, list)
    assert len(users) > 0
