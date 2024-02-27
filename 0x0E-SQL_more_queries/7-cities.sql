-- Create database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switch to the newly created or existing database
USE hbtn_0d_usa;

-- Create a table to store city data
CREATE TABLE IF NOT EXISTS cities (
    -- Unique identifier for each city, auto-incremented
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    -- Identifier for the state to which the city belongs
    state_id INT NOT NULL,
    -- Name of the city
    name VARCHAR(256) NOT NULL,
    -- Define a foreign key constraint referencing the id column in the states table
    FOREIGN KEY (state_id) REFERENCES states(id)
);
