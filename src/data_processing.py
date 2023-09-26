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

"""

import csv
from collections import Counter
from collections import defaultdict


def read_csv(file_path):
    """Read .csv file and return data as dicitonary list"""
    with open(file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        data = [row for row in csv_reader]
    return data, data

def count_offences(data):
    """Count offence occurences from OFNS_DESC"""
    offence_desc = [row['OFNS_DESC'] for row in data]
    return Counter(offence_desc)

def sort_offence_desc(counter):
    """Sort offences in descending order"""
    return counter.most_common()

def get_top_ten_offences(sorted_offences):
    """Get top first 10 items of a sorted offence list"""
    return sorted_offences[:10]

def arrest_count_age_pd_cd(data):
    """Arrest count by age group and PD_CD"""
    counter = defaultdict(lambda: defaultdict(int))
    for row in data:
        counter[row['AGE_GROUP']][row['PD_CD']] += 1
    return counter

def fourth_greatest_arrests(counter):
    """Fourth highest arrest count for an age group by PD_CD"""
    fourth_highest = {}
    for age_group, pd_cd_count in counter.items():
        sorted_counts = sorted(pd_cd_count.items(), key=lambda x: x[1], reverse=True)
        if len(sorted_counts) >= 4:
            fourth_highest[age_group] = sorted_counts[3]
    return fourth_highest