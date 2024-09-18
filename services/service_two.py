import requests


def get_users():
    """
    Fetch users from JSONPlaceholder API.

    Returns:
        list: A list of users.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    response.raise_for_status()
    return response.json()
