"""

Functions to fulfill the user interaction activities of the task 

Actions:
4. Allow user input to run all of your script, or specific sections

"""

import csv


def get_user_input():
    """Get user input of option choice"""
    print("Choose an option:")
    print("1. View Top 10 Offenses")
    print("2. View Arrests by Age and PD Code")
    print("3. Export Data to CSV")
    print("4. Import Data to SQLite DB")
    print("5. Quit \n")
    return input()

def get_offence_desc():
    """Get uer input of offence"""
    return input("\n Enter the full or partial offence description: ")
