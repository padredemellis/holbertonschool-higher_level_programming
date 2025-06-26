-- Script para crear el usuario 'user_0d_1' en el servidor MySQL local (localhost).
-- El usuario tendrá todos los privilegios y su contraseña será 'user_0d_1_pwd'.
-- El script no fallará si el usuario ya existe, ya que lo borrará y recreará.

-- 1. Borrar el usuario 'user_0d_1' si existe.
-- Esto asegura una creación limpia cada vez y evita errores si el usuario
-- existe con configuraciones previas o una contraseña diferente.
DROP USER IF EXISTS 'user_0d_1'@'localhost';

-- 2. Crear el usuario 'user_0d_1' con su contraseña.
-- Ahora que sabemos que el usuario no existe, podemos crearlo directamente.
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- 3. Otorgar todos los privilegios al usuario 'user_0d_1'.
-- 'ALL PRIVILEGES' concede todos los permisos disponibles.
-- 'ON *.*' significa en todas las bases de datos y todas las tablas.
-- 'TO 'user_0d_1'@'localhost'' especifica a qué usuario y desde qué host se le otorgan los permisos.
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- 4. Recargar los privilegios en el servidor MySQL.
-- Esto es crucial para que los cambios en los permisos (GRANT) surtan efecto inmediatamente
-- sin necesidad de reiniciar el servidor MySQL.
FLUSH PRIVILEGES;