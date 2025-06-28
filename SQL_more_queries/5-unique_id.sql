-- unique id
CREATE DATABASE IF NOT EXISTS hbtn_test_db_5;
CREATE TABLE IF NOT EXISTS hbtn_test_db_5.unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);