"""
This project demonstrates the ability to interact with a SQL database using SQLite.
It includes creating a database, defining a schema, and executing various SQL commands.
Logging is incorporated to document the process.
"""

import sqlite3
import pandas as pd
import pathlib
import logging

# Configure logging
logging.basicConfig(
    filename='log.txt',
    level=logging.DEBUG,
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("Program started")

# Define the database file in the current root project directory
db_file = pathlib.Path("project.db")

def create_database():
    """Create the database."""
    try:
        conn = sqlite3.connect(db_file)
        conn.close()
        logging.info("Database created successfully.")
    except sqlite3.Error as e:
        logging.exception("Error creating the database: %s", e)

def create_tables():
    """Read and execute SQL statements to create tables."""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql", "create_tables.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            logging.info("Tables created successfully.")
    except sqlite3.Error as e:
        logging.exception("Error creating tables: %s", e)
    except FileNotFoundError as e:
        logging.exception("SQL file not found: %s", e)

def insert_data_from_csv():
    """Read data from CSV files and insert into tables."""
    try:
        author_data_path = pathlib.Path("data", "authors.csv")
        book_data_path = pathlib.Path("data", "books.csv")
        authors_df = pd.read_csv(author_data_path)
        books_df = pd.read_csv(book_data_path)
        with sqlite3.connect(db_file) as conn:
            authors_df.to_sql("authors", conn, if_exists="replace", index=False)
            books_df.to_sql("books", conn, if_exists="replace", index=False)
            logging.info("Data inserted successfully.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        logging.exception("Error inserting data: %s", e)

def main():
    create_database()
    create_tables()
    insert_data_from_csv()
    logging.info("Database initialization completed successfully.")

if __name__ == "__main__":
    main()