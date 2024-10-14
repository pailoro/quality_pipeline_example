from tenacity import retry, stop_after_attempt, wait_fixed

from services import service_two


@retry(wait=wait_fixed(2), stop=stop_after_attempt(3))
def test_user_structure():
    """
    Test the structure of a user-.
    """
    users = service_two.get_users()
    assert len(users) > 0, "The API returned an empty list of users."
    user = users[0]
    assert "id" in user
    assert "name" in user
    assert "username" in user
    assert "email" in user
