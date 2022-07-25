import unittest
from unittest.mock import Mock
from todo_v2 import DatabaseManager
import psycopg2

class TestDatabaseManager(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.db = psycopg2.connect(**{
            'dbname': 'todo_app',
            'user': 'postgres',
            'password': 'password',
            'port': '54320',
            'host': 'localhost'
        })
        cls.db_manager = DatabaseManager(cls.db)

    def setUp(self):
        with self.db.cursor() as cur:
            cur.execute('TRUNCATE todo')
        self.db.commit()

    def test_insert_and_get_todos(self):
        self.db_manager.insert_todo('todo')
        todos = self.db_manager.get_todos()
        assert todos[0][1] == 'todo'

if __name__ == '__main__':
    unittest.main()
