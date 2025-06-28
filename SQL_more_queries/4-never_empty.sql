-- Asegura la existencia de la base de datos específica
CREATE DATABASE IF NOT EXISTS hbtn_test_db_4;

-- Crea la tabla en la base de datos correcta
CREATE TABLE IF NOT EXISTS hbtn_test_db_4.id_not_null (
    id INT NOT NULL DEFAULT 1,
    name VARCHAR(256)
);