-- Create database first.
CREATE DATABASE to_do_list_db;

-- Drop tables if they already exist.
DROP TABLE IF EXISTS completed;
DROP TABLE IF EXISTS in_progress;
DROP TABLE IF EXISTS to_do;

-- Create tables
CREATE TABLE to_do(
    to_do_id SERIAL PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL
);

CREATE TABLE in_progress(
    in_progress_id SERIAL PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL
);

CREATE TABLE completed(
    completed_id SERIAL PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL
);

-- Insert values into the tables
INSERT INTO to_do(item_name) VALUES
('Test One'),
('Test Two');

INSERT INTO in_progress(item_name) VALUES
('Testing One'),
('Testing Two');

INSERT INTO completed(item_name) VALUES
('Tested One'),
('Tested Two');

-- Command to run in the terminal to run the sql file 'psql -U *username*(i.e. postgres or specific user) -d *database name* -f *filename*.sql'
-- In this example it will be 'psql -U to_do_list_dev -d to_do_list_db -f to_do_list.sql'