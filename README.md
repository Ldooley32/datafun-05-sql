# datafun-05-sql
 create Repository named datafun-05-sql

Option 1

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

# add the following to requirements.txt
    '''jcsv
       pathlib
       sqlite3
       uuid
       panadas'''
>install pandas make sure virtual environment is activated
    '''python3 -m pip install pandas pyarrow'''

> freeze dependency in the requirements.txt may cause errors for this project.
    '''python3 -m pip freeze > requirements.txt'''

Add a folder for data.
    create 2 csv files: aurthors.csv and books.csv

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
