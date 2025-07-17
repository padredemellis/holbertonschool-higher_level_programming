import sqlite3
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def create_database():
    """Crea y popula la base de datos SQLite 'products.db' con datos de ejemplo."""
    db_file = 'products.db'
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # Crear la tabla Products si no existe
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')
        logging.info("Table 'Products' ensured to exist.")

        # Insertar datos de ejemplo, solo si la tabla está vacía para evitar duplicados
        cursor.execute("SELECT COUNT(*) FROM Products")
        if cursor.fetchone() == 0:
            cursor.execute('''
                INSERT INTO Products (id, name, category, price)
                VALUES
                (1, 'Laptop', 'Electronics', 799.99),
                (2, 'Coffee Mug', 'Home Goods', 15.99),
                (3, 'Mechanical Keyboard', 'Electronics', 120.00)
            ''')
            conn.commit()
            logging.info("Sample data inserted into 'Products' table.")
        else:
            logging.info("Table 'Products' already contains data, skipping insertion.")

    except sqlite3.Error as e:
        logging.error(f"SQLite error during database creation: {e}")
    except Exception as e:
        logging.error(f"Unexpected error during database creation: {e}")
    finally:
        if conn:
            conn.close()
            logging.info(f"Database connection to {db_file} closed.")

if __name__ == '__main__':
    create_database()