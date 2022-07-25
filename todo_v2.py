import os
import psycopg2

def generate_todo(db_manager):
    todos = db_manager.get_todos()
    if not todos:
        db_manager.insert_todo('Add todos')

class DatabaseManager:
    def __init__(self, db):
        self.db = db

    def get_todos(self):
        with self.db.cursor() as cur:
            cur.execute('SELECT * FROM todo;')
            results = cur.fetchall()
        return results

    def insert_todo(self, description):
        with self.db.cursor() as cur:
            cur.execute('INSERT INTO todo (description) VALUES (%s)', (description,))
        self.db.commit()

if __name__ == '__main__':
    db = psycopg2.connect(**{
        'dbname': 'todo_app',
        'user': os.environ.get('DB_USER'),
        'password': os.environ.get('DB_PASSWORD'),
        'port': '54320',
        'host': 'localhost'
    })


    db_manager = DatabaseManager(db)
    generate_todo(db_manager)
    print(db_manager.get_todos())
