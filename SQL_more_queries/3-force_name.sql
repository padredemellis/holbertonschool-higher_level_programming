-- 3-force_name.sql
CREATE DATABASE IF NOT EXISTS hbtn_test_db_3;
USE hbtn_test_db_3;
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);