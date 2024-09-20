from tenacity import retry, stop_after_attempt, wait_fixed

from services import service_three


@retry(wait=wait_fixed(2), stop=stop_after_attempt(3))
def test_todo_structure():
    """
    Test the structure of a todo.
    """
    todos = service_three.get_todos()
    assert len(todos) > 0, "The API returned an empty list of todos."
    todo = todos[0]
    assert "userId" in todo
    assert "id" in todo
    assert "title" in todo
    assert "completed" in todo
