-- Creates the MySQL user user_0d_1 with all the privileges on the server.
-- Create the user, without failing if it already exists.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Give the user all the privileges on the server.
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
