import yaml
from pathlib import Path

'''
    SETUP FILENAME BELOW
'''
filename = 'clickup_shots_list_template' + '.yml'




with open(filename) as file:
    values = yaml.load(file, Loader=yaml.FullLoader)

print('Full Loader: {}'.format(values))

values = values.replace('0000000000000', '9999999999999')

print('Full Loader: {}'.format(values))