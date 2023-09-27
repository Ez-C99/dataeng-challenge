"""

Functions to fulfill the database operation activities of the task 

Requirements:
4. Instantiate a sqlite db and insert all records from the original csv into it.

"""

import sqlite3

def create_db_and_table(db_name):
    """Create SQLite database and table to store arrests"""
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE arrests (
            ARREST_KEY INTEGER PRIMARY KEY,
            AGE_GROUP TEXT,
            PD_CD TEXT,
            OFNS_DESC TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_in_db(data, db_name):
    """Insert data in SQLite database"""
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    for row in data:
        c.execute("INSERT INTO arrests (ARREST_KEY, AGE_GROUP, PD_CD, OFNS_DESC) VALUES (?, ?, ?, ?)",
                  (row['ARREST_KEY'], row['AGE_GROUP'], row['PD_CD'], row['OFNS_DESC']))
    conn.commit()
    conn.close()