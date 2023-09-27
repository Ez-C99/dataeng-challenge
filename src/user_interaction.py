"""

Functions to fulfill the user interaction activities of the task 

Actions:
4. Allow user input to run all of your script, or specific sections

"""

import csv


def get_user_input():
    """Get user input of main menu choice"""
    print("\n Choose an option:")
    print("1. View Top 10 Offenses")
    print("2. View 4th Most Arrests by PD Code for each Age Group")
    print("3. Export Data to CSV")
    print("4. Import Data to SQLite DB")
    print("5. Quit \n")
    return input()

def get_offence_desc():
    """Get user input of offence description"""
    return input("\n Enter the full or partial offence description: ")
