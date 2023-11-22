-- A script that prepares a MySQL server for the project
-- MySQL setup test_db


-- Creates a database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Drop user if it exists
DROP USER IF EXISTS 'hbnb_test'@'localhost';
-- Create a new user in localhost, and set the password for the new user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED WITH mysql_native_password BY 'hbnb_test_pwd';
-- Grant new user privileges on the database, and only the database
GRANT ALL PRIVILEGES ON hbnb_test_db. * TO 'hbnb_test'@'localhost';
-- Grant new user SELECT privilege on db performance_schema
GRANT SELECT ON performance_schema. * TO 'hbnb_test'@'localhost';
-- Flush privileges to apply changes
FLUSH PRIVILEGES;
