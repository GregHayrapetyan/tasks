import unittest
import filecmp
from task1 import *
class Test_Converter(unittest.TestCase):
    def test_json_file(self):
        yaml_file = 'yaml_file_test'
        json_to_yaml_converter('json_file.json', yaml_file)
        filecmp.cmp('yaml_file', 'yaml_file_test')
if __name__ == '__main__':
    unittest.main()