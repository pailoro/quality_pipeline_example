from services import service_one


def test_post_structure():
    """
    Test the structure of a post.
    """
    posts = service_one.get_posts()
    post = posts[0]
    assert "userId" in post
    assert "id" in post
    assert "title" in post
    assert "body" in post
