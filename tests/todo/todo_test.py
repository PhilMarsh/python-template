import pytest

from todo.todo import TODO


@pytest.fixture
def a_todo():
    return TODO()


class TestTODO:
    def test_todo(self, a_todo):
        assert isinstance(a_todo, TODO)
