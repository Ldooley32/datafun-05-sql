## Project 5
 
# Overview 

Intergrating Python and SQL, to perform various SQL operations that will create and manage databases. Will use SQLite for quieres with joins, filters, and aggregations. Logging to help manage and debug project. 

# Objective

- Create and clone a repository

Use GitHub 
1. under repository click new
2. Add repo name
3. Make public 
4. Create README.md file 
5. Add .gitignore file using phython template

# Clone repo in using terminal 
1. open terminal in the documents to store repe
    '''cd documents''
2. clone repo 
    '''git clone https://github.com/Ldooley32/datafun-05-sql'''
3. open repo folder using VS code.
4. add requirements.txt
5. Create a virtual environment
    ''' python3 -m venv .venv'''
6. activate environment
    ''' source .venv/bin/sctivate'''
7. push chages to GitHub
    ''' git add .
        git commit -m "informative message"
        git push origin main'''

- Initialize script: db_initialize_yourname.py
- Operations script: db_operations_yourname.py

# 1. Project Start

Add a docstring to introduce project

# 2. Import Dependencies 
    '''jcsv
       pathlib
       sqlite3
       uuid
       panadas'''
>install pandas make sure virtual environment is activated
    '''python3 -m pip install pandas pyarrow'''

> freeze dependency in the requirements.txt may cause errors for this project.
    '''python3 -m pip freeze > requirements.txt'''

# 3. Logging
    1. Configure logging to write to a file named log.txt.
    2. Log the start of the program using logging.info().
    3. Log the end of the program using logging.info().
    4. Log exceptions using logging.exception().
    5. Log other major events using logging.info().
    6. Log the start and end of major functions using logging.debug().

# 4. Schema Design and Database Creation
    1. Create databases 
    2. Creat Tables (2 tables include foreign key restraints)
    3. Populate tables 
    4. keep SQL statements in separate files

# 5. SQL Operations 
    use python to execute SQL Statements
    include the following SQL files 
        1. create_tables.sql - create your database schema using sql
        2. insert_records.sql - insert at least 10 additional records into each table.
        3. update_records.sql - update 1 or more records in a table.
        4. delete_records.sql - delete 1 or more records from a table.
        5. query_aggregation.sql - use aggregation functions including COUNT, AVG, SUM.
        6. query_filter.sql - use WHERE to filter data based on conditions.
        7. query_sorting.sql - use ORDER BY to sort data.
        8.query_group_by.sql - use GROUP BY clause (and optionally with aggregation)
        9. query_join.sql - use INNER JOIN operation and optionally include LEFT JOIN, RIGHT JOIN, etc.

# 6. Python and SQL intergation 
    define a function to for python to interact with SQL 
    '''import sqlite3

def execute_sql_from_file(db_filepath, sql_file):
    with sqlite3.connect(db_filepath) as conn:
        with open(sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file}") '''

# 7. Define main functions for SQL operations 
    '''
def main():
    db_filepath = 'your_database.db'

    # Create database schema and populate with data
    execute_sql_from_file(db_filepath, 'insert_records.sql')
    execute_sql_from_file(db_filepath, 'update_records.sql')
    execute_sql_from_file(db_filepath, 'delete_records.sql')
    execute_sql_from_file(db_filepath, 'query_aggregation.sql')
    execute_sql_from_file(db_filepath, 'query_filter.sql')
    execute_sql_from_file(db_filepath, 'query_sorting.sql')
    execute_sql_from_file(db_filepath, 'query_group_by.sql')
    execute_sql_from_file(db_filepath, 'query_join.sql')

    logging.info("All SQL operations completed successfully")'''


# 8. Conditional script Execution 
    '''if __name__ == "__main__":
            main()'''





# Initialize the Project Database
    create subfolders for our SQL statements, our data files, and we'll keep our Python scripts in the root project folder
datafun-05-sql/
│
├── data/
│   ├── authors.csv
│   └── books.csv
│
├── sql/
│   ├── create_tables.sql
│   ├── insert_records.sql (not used when we read data from csv, but good to see)
│
├── project.db
├── book_manager.py

# Creating a Database from Data at Rest
On your machine, open your project repository folder in VS Code. In the root project repository folder, create a Python file (module and script) named book_manager.py. 
    copy over code
create a SQL file named create_tables.sql    
    copy over code
