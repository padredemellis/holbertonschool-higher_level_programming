-- Never empty
CRESATE TABLE IF NOT EXISTS id_not_null(
    ID INT NOT NULL DEFAULT 1,
    name VARCHAR(256)
);