import unittest
import xmlrunner
import os
import sys

parent_path = os.path.dirname(sys.path[0])
if parent_path not in sys.path:
    sys.path.append(parent_path)

from api_functionality_support.forcast_api import ForcastAPI
from support import utils

class ForcastApi(unittest.TestCase):
    def test_forcast(self):
        print(f'parent path: {parent_path}')
        forcast_api = ForcastAPI()
        response_status = forcast_api.get_forcast_response_status()
        self.assertEqual(response_status, 200, "Response status is not successfull!")
        print(forcast_api.get_relative_humidity_the_day_after_tomorrow())

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite(loader.loadTestsFromTestCase(ForcastApi))
    report_folder = utils.check_xml_report_folder()
    runner = xmlrunner.XMLTestRunner(output=report_folder)
    runner.run(suite)