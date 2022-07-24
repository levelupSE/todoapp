CREATE DATABASE todo_app;

\c todo_app;

CREATE TABLE IF NOT EXISTS todo (
  todo_id UUID PRIMARY KEY,
  description TEXT NOT NULL
);

