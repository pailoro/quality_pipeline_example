import requests


def get_todos():
    """
    Fetch todos from JSONPlaceholder API.

    Returns:
        list: A list of todos.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    response.raise_for_status()
    return response.json()
