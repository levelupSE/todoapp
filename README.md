# TODO App

# Set up
- Install poetry: https://python-poetry.org/docs/#installation
- Install dependencies with `poetry install`

# Running locally
- `docker-compose up` to start database
- Remove `postgres_data` if you want `scripts/init.sql` to run again
- `poetry shell` to activate virtual environment
- `DB_USER=postgres DB_PASSWORD=password python todo_v1.py` to run v1
- `DB_USER=postgres DB_PASSWORD=password python todo_v2.py` to run v2
- `PGPASSWORD=password psql -U postgres -d todo_app -h localhost -p 54320 -c 'TRUNCATE todo'` to clear table

# Running test
- `python test_generate_todo.py -v`
- `python test_database_manager.py -v`
