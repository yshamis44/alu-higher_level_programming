-- Creates the table force_name where the name can not be null.
-- Create the table, without failing if it already exists.
CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);
