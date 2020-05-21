import yaml
from pathlib import Path

'''
    SETUP FILENAME BELOW
'''
filename = 'clickup_assets_list_template' + '.yml'


'''
    SETUP THE VARIABLE BELOW
'''
values = """
  {
    "name": "ASSETS",
    "content": "Assets List",
    "due_date": 0000000000000,
    "due_date_time": false,
    "priority": 3,
    "assignee": 0,
    "status": "yellow"
  }
"""

'''
    RUN THE CODE
'''

with open(filename, 'w') as yaml_file:
    yaml.dump(values, yaml_file, default_flow_style=False)