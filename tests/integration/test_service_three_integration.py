from services import service_three


def test_todo_structure():
    """
    Test the structure of a todo.
    """
    todos = service_three.get_todos()
    todo = todos[0]
    assert "userId" in todo
    assert "id" in todo
    assert "title" in todo
    assert "completed" in todo
