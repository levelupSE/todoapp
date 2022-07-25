import unittest
from unittest.mock import Mock
from todo_v2 import generate_todo

class TestGenerateTodo(unittest.TestCase):

    def test_if_no_todos_creates_todo(self):
        db_manager = Mock()
        db_manager.get_todos.return_value = []

        generate_todo(db_manager)

        db_manager.get_todos.assert_called()
        db_manager.insert_todo.assert_called_with('Add todos')

    def test_if_todos_does_not_creates_todo(self):
        db_manager = Mock()
        db_manager.get_todos.return_value = [(1, 'todo')]

        generate_todo(db_manager)

        db_manager.get_todos.assert_called()
        db_manager.insert_todo.assert_not_called()

if __name__ == '__main__':
    unittest.main()
