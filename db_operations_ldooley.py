import sqlite3
import logging

# Configure logging
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

def execute_sql_from_file(db_filepath, sql_file):
    """Execute SQL commands from a file."""
    try:
        with sqlite3.connect(db_filepath) as conn:
            with open(sql_file, 'r') as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            logging.info(f"Executed SQL from {sql_file}")
    except sqlite3.Error as e:
        logging.exception(f"Error executing SQL from {sql_file}: %s", e)
    except FileNotFoundError as e:
        logging.exception(f"SQL file not found: {sql_file}")

def main():
    db_filepath = 'project.db'

    execute_sql_from_file(db_filepath, 'sql/insert_records.sql')
    execute_sql_from_file(db_filepath, 'sql/update_records.sql')
    execute_sql_from_file(db_filepath, 'sql/delete_records.sql')
    execute_sql_from_file(db_filepath, 'sql/query_aggregation.sql')
    execute_sql_from_file(db_filepath, 'sql/query_filter.sql')
    execute_sql_from_file(db_filepath, 'sql/query_sorting.sql')
    execute_sql_from_file(db_filepath, 'sql/query_group_by.sql')
    execute_sql_from_file(db_filepath, 'sql/query_join.sql')

    logging.info("All SQL operations completed successfully")

if __name__ == "__main__":
    main()
    logging.info("Program ended")
