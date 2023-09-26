"""

Functions to fulfill the database operation activities of the task 

Requirements:
4. Instantiate a sqlite db and insert all records from the original csv into it.

"""

import sqlite3

def create_db_and_table(db_name):
    """Create SQLite database and table"""
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS arrests
                 (OFNS_DESC TEXT, AGE_GROUP TEXT, PD_CD TEXT)''')
    conn.commit()
    conn.close()

def insert_in_db(data, db_name):
    """Insert data in SQLite database"""
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    for row in data:
        c.execute("INSERT INTO arrests (OFNS_DESC, AGE_GROUP, PD_CD) VALUES (?, ?, ?)",
                  (row['OFNS_DESC'], row['AGE_GROUP'], row['PD_CD']))
    conn.commit()
    conn.close()