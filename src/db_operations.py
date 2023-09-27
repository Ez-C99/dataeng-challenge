"""

Functions to fulfill the database operation activities of the task 

Requirements:
4. Instantiate a sqlite db and insert all records from the original csv into it.

"""

import sqlite3
from constants import EXPORT_FOLDER

def create_db_and_table(db_name):
    """Create SQLite database and table to store arrests"""
    full_path = f'{EXPORT_FOLDER}{db_name}'
    conn = sqlite3.connect(full_path)
    c = conn.cursor()

    # Drop the existing table if it exists so table creation capabilities are always demonstrated
    c.execute('DROP TABLE IF EXISTS arrests')

    # Create new table
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
    full_path = f'{EXPORT_FOLDER}{db_name}'
    conn = sqlite3.connect(full_path)
    c = conn.cursor()
    for row in data:
        c.execute("INSERT INTO arrests (ARREST_KEY, AGE_GROUP, PD_CD, OFNS_DESC) VALUES (?, ?, ?, ?)",
                  (row['ARREST_KEY'], row['AGE_GROUP'], row['PD_CD'], row['OFNS_DESC']))
    conn.commit()
    conn.close()