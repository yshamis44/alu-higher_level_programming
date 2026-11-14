-- Creates the table unique_id where the id has the default value 1 and must be unique.
-- Create the table, without failing if it already exists.
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
