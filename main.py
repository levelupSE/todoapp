import psycopg2

if __name__ == '__main__':
    db = psycopg2.connect(**{
        'dbname': 'todo_app',
        'password': 'password',
        'user': 'postgres',
        'port': '54320',
        'host': 'localhost'
    })
    with db.cursor() as cur:
        cur.execute('SELECT * FROM todo;')
        results = cur.fetchall()

    print(f'Results: {results}')
