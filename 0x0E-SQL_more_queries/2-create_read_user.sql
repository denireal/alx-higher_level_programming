-- Create or check if the database hbtn_0d_2 exists, and create it if it
-- doesn't
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create or check if the user user_0d_2 exists, and create it with the
-- specified password if it doesn't
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant the SELECT privilege on the database hbtn_0d_2 to the user user_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Flush the privileges to apply the changes
FLUSH PRIVILEGES;
