-- Creates the database hbtn_0d_2 and the user user_0d_2 who can only read it.
-- Create the database, without failing if it already exists.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Create the user, without failing if it already exists.
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Give the user the SELECT privilege only, and only on hbtn_0d_2.
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
