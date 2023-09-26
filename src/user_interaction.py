"""

Functions to fulfill the user interaction activities of the task 

Actions:
4. Allow user input to run all of your script, or specific sections

Requirements:
3. Export to a csv file containing user specified OFNS_DESC. For example, a user can specify full or part of an offence - 'ASSAULT' or 'ASSAULT 3' or 'ASSAULT 3 & RELATED'. Export the result to a csv file.

"""

import csv


def get_user_input(prompt):
    """Get user input"""
    return input(prompt)

def filter_offences_by_input(counter, input):
    """Filter offences by user input"""
    return {k: v for k, v in counter.items() if input.lower() in k.lower()}

def export_to_csv(data, file_path):
    """Export data to a .csv file"""
    with open(file_path, mode='w', newline=' ') as f:
        writer = csv.writer(f)
        writer.writerow(['Offence Description', 'Count'])
        for k, v in data.items():
            writer.writerow([k, v])