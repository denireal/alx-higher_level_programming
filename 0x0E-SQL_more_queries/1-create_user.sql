-- Creates a new MySQL user and grants all privileges on all dbs and tables.
-- Create a new user 'user_0d_1' with the password 'user_0d_1_pwd' and allow
-- access only from 'localhost'
-- Grant all privileges on all databases and tables to the user 'user_0d_1'
-- when accessing from 'localhost'

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
