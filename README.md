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

> Will not freeze dependency in the requirements.txt may cause errors for this project.
    '''python3 -m pip freeze > requirements.t
    