import os
import psycopg2

db = psycopg2.connect(**{
    'dbname': 'todo_app',
    'user': os.environ.get('DB_USER'),
    'password': os.environ.get('DB_PASSWORD'),
    'port': '54320',
    'host': 'localhost'
})

def generate_todo():
    # get todos from database
    with db.cursor() as cur:
        cur.execute('SELECT * FROM todo;')
        todos = cur.fetchall()

    # if there are no todos, create a todo to add more todos
    if not todos:
        with db.cursor() as cur:
            cur.execute('INSERT INTO todo (description) VALUES (%s)', ('Add todos',))
        db.commit()

if __name__ == '__main__':
    generate_todo()
