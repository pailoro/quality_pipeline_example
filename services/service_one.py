import requests


def get_posts():
    """
    Fetch posts from JSONPlaceholder API -.

    Returns:
        list: A list of posts.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    response.raise_for_status()
    return response.json()
