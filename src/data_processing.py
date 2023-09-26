"""

Functions to fulfill the data processing activities of the task

Actions:
1. Load the data file, process and output the data in the forms specified
2. Read in, process and present the data as specified in the requirements section
3. Demonstrate usage of list comprehension for at least one of the tasks

Requirements:
1. Read in the attached file
    - Produce a dictionary count records group by OFNS_DESC in descending order
    - Obtain the first 10 items from the resultant list and output to the console
2. Obtain the count of arrests grouped by age group and PD_CD. Find the 4th greatest number of arrests by PD_CD for each age group and output to the console.
3. Export to a csv file containing user specified OFNS_DESC. For example, a user can specify full or part of an offence - 'ASSAULT' or 'ASSAULT 3' or 'ASSAULT 3 & RELATED'. Export the result to a csv file.

"""

import csv
from collections import Counter


def read_csv(file_path):
    """Read .csv file and return data as dicitonary list"""
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        data = [row for row in csv_reader]
    return data

def count_offences(data):
    """Count offence occurences from OFNS_DESC"""
    offence_desc = [row['OFNS_DESC'] for row in data]
    return Counter(offence_desc)

# def sort_offence_desc(counter):
#     """Sort offences in descending order"""
#     return counter.most_common()

# def get_top_ten_offences(sorted_offences):
#     """Get top first 10 items of a sorted offence list"""
#     return sorted_offences[:10]

def arrest_count_age_pd_cd(data):
    age_code_dict = {}
    for row in data:
        age_group = row['AGE_GROUP']
        pd_code = row['PD_CD']
        if age_group not in age_code_dict:
            age_code_dict[age_group] = {}
        if pd_code not in age_code_dict[age_group]:
            age_code_dict[age_group][pd_code] = 0
        age_code_dict[age_group][pd_code] += 1
    return age_code_dict

# def fourth_greatest_arrests(counter):
#     """Fourth highest arrest count for an age group by PD_CD"""
#     fourth_highest = {}
#     for age_group, pd_cd_count in counter.items():
#         sorted_counts = sorted(pd_cd_count.items(), key=lambda x: x[1], reverse=True)
#         if len(sorted_counts) >= 4:
#             fourth_highest[age_group] = sorted_counts[3]
#     return fourth_highest

def filter_by_offence(data, offence_desc):
    """Filter offences by user input"""
    return [row for row in data if offence_desc.lower() in row['OFNS_DESC'].lower()]

def export_to_csv(data, file_path):
    """Export data to a .csv file"""
    with open(file_path, mode='w', newline=' ') as f:
        writer = csv.writer(f)
        writer.writerow(['Offence Description', 'Count'])
        for k, v in data.items():
            writer.writerow([k, v])