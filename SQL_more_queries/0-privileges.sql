-- Script para listar todos los privilegios de los usuarios user_0d_1 y user_0d_2
-- en el servidor MySQL local (localhost).

-- Muestra los privilegios para user_0d_1 en localhost.
-- Si el usuario no existe o no tiene grants definidos, MySQL arrojará un error 1141.
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Muestra los privilegios para user_0d_2 en localhost.
-- Al igual que con user_0d_1, si el usuario no existe o no tiene grants, se mostrará un error.
SHOW GRANTS FOR 'user_0d_2'@'localhost';