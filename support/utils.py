import time
import os
import sys

parent_path = os.path.dirname(sys.path[0])
today = time.strftime("%Y%m%d")

def check_xml_report_folder():
    print("project_folder:",parent_path)
    reportPath = parent_path + "/xml_report/" + today
    print(f'report path:{reportPath}')
    if not os.path.exists(reportPath):
        os.makedirs(reportPath)
    return reportPath + "/"