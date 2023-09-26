import unittest
from src import data_processing as dp

class TestDataProcessingFunctions(unittest.TestCase):

    def test_read_csv(self):
        data = dp.read_csv('data/nypd-arrest-data-2018-1.csv')
        self.assertIsNotNone(data)
        self.assertTrue('OFNS_DESC' in data[0])
        self.assertTrue('AGE_GROUP' in data[0])

    def test_count_offences(self):
        data = [{'OFNS_DESC': 'THEFT'}, {'OFNS_DESC': 'THEFT'}, {'OFNS_DESC': 'FRAUD'}]
        result = dp.count_offenses(data)
        self.assertEqual(result, {'THEFT': 2, 'FRAUD': 1})

    def test_arrest_count_age_pd_cd(self):
        data = [
            {'AGE_GROUP': '25-30', 'PD_CD': '101'},
            {'AGE_GROUP': '25-30', 'PD_CD': '102'},
            {'AGE_GROUP': '25-30', 'PD_CD': '101'},
            {'AGE_GROUP': '30-35', 'PD_CD': '101'}
        ]
        result = dp.count_arrests_by_age_and_code(data)
        self.assertEqual(result, {'25-30': {'101': 2, '102': 1}, '30-35': {'101': 1}})