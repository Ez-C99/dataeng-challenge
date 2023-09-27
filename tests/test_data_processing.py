import os
import unittest
from src import data_processing as dp


class TestDataProcessingFunctions(unittest.TestCase):

    def test_read_csv(self):
        """
        Test that the read_csv function can successfully read the CSV file and return a list of dictionaries.
        
        Check if the returned data is not None and contains specific keys ('OFNS_DESC' and 'AGE_GROUP').
        """
        data = dp.read_csv('data/nypd-arrest-data-2018-1.csv')
        self.assertIsNotNone(data)
        self.assertTrue('OFNS_DESC' in data[0])
        self.assertTrue('AGE_GROUP' in data[0])

    def test_count_offences(self):
        """
        Test that the count_offences function returns a counter of offences as expected.
        
        Feed in a list of dictionaries containing offence descriptions and check counter reflects the
        frequencies correctly.
        """
        data = [{'OFNS_DESC': 'THEFT'}, {'OFNS_DESC': 'THEFT'}, {'OFNS_DESC': 'FRAUD'}]
        result = dp.count_offences(data)
        self.assertEqual(result, {'THEFT': 2, 'FRAUD': 1})

    def test_arrest_count_age_pd_cd(self):
        """
        Test that the arrest_count_age_pd_cd function groups and counts the data by age and PD code correctly.
        
        Use sample data set and check function to returns a dictionary that groups counts by
        age group and PD code.
        """
        data = [
            {'AGE_GROUP': '25-30', 'PD_CD': '101'},
            {'AGE_GROUP': '25-30', 'PD_CD': '102'},
            {'AGE_GROUP': '25-30', 'PD_CD': '101'},
            {'AGE_GROUP': '30-35', 'PD_CD': '101'}
        ]
        result = dp.arrest_count_age_pd_cd(data)
        self.assertEqual(result, {'25-30': {'101': 2, '102': 1}, '30-35': {'101': 1}})

    def test_filter_by_offence(self):
        """
        Test that the filter_by_offence function filters the records based on a given offence description.
        
        Check that only records matching the filter will be returned.
        """
        data = [
            {'OFNS_DESC': 'ASSAULT 1'},
            {'OFNS_DESC': 'ASSAULT 2'},
            {'OFNS_DESC': 'THEFT'}
        ]
        result = dp.filter_by_offence(data, 'ASSAULT')
        self.assertEqual(len(result), 2)

    def test_export_to_csv(self):
        """
        Test that the export_to_csv function correctly exports data to a CSV file.
        
        Export a sample dataset to a .csv file, then reads the file to verify that
        the data was successfully written.
        """
        data = [
            {'OFNS_DESC': 'ASSAULT 1'},
            {'OFNS_DESC': 'ASSAULT 2'},
        ]
        dp.export_to_csv(data, 'test_export.csv')
        read_data = dp.read_csv('test_export.csv')
        self.assertEqual(len(read_data), 2)
        # Delete test file to remove residual files if required
        # os.remove('test_export.csv')