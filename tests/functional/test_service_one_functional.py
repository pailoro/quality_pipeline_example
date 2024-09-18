from services import service_one


def test_get_posts():
    """
    Test the get_posts function.
    """
    posts = service_one.get_posts()
    assert isinstance(posts, list)
    assert len(posts) > 0
