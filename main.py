import psycopg2

db = psycopg2.connect(**{
    'dbname': 'todo_app',
    'password': 'password',
    'user': 'postgres',
    'port': '54320',
    'host': 'localhost'
})

def get_todos():
    with db.cursor() as cur:
        cur.execute('SELECT * FROM todo;')
        results = cur.fetchall()
    return results

def insert_todo(description):
    with db.cursor() as cur:
        cur.execute('INSERT INTO todo (description) VALUES (%s)', (description,))

def get_homepage_message():
    todos = get_todos()
    if not todos:
        return 'All your TODOs are done!'

    todo_descriptions = ', '.join([todo[1] for todo in todos])
    return f'Here are your todos: {todo_descriptions}'

if __name__ == '__main__':
    print(get_homepage_message())
    insert_todo('something')
    print(get_homepage_message())
    insert_todo('something1')
    print(get_homepage_message())
