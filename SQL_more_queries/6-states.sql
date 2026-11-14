-- Creates the database hbtn_0d_usa and the table states in it.
-- Create the database, without failing if it already exists.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Create the table, without failing if it already exists.
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
