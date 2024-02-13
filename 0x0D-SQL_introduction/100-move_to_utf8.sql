-- Sets the current database context to hbtn_0c_0
-- Alters the table first_table to use utf8mb4 character set
-- and utf8mb4_unicode_ci collation
USE hbtn_0c_0
ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
