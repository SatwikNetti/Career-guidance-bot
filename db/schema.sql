-- Simple PostgreSQL schema for storing users and api keys
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS api_keys (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    api_key TEXT NOT NULL,
    label TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
