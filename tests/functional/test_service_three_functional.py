from services import service_three


def test_get_todos():
    """
    Test the get_todos function.
    """
    todos = service_three.get_todos()
    assert isinstance(todos, list)
    assert len(todos) > 0
