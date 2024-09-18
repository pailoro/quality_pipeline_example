from services import service_one
from tenacity import retry, wait_fixed, stop_after_attempt

@retry(wait=wait_fixed(2), stop=stop_after_attempt(3))
def test_post_structure():
    """
    Test the structure of a post.
    """
    posts = service_one.get_posts()
    assert len(posts) > 0, "The API returned an empty list of posts."
    post = posts[0]
    assert "userId" in post
    assert "id" in post
    assert "title" in post
    assert "body" in post
    print(posts)
