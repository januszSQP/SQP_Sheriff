import urllib.request
import certifi
import ssl
import json
from pathlib import Path
import yaml
from importlib.util import spec_from_loader, module_from_spec
from importlib.machinery import SourceFileLoader
import pickle




show_title = 'FORCE DUPSKO'

path_config = Path(__file__).parent / "clickup_api.json"
path_clickup_space_template = Path(__file__).parent / "clickup_space_template.pckl"
path_clickup_shots_list_template = Path(__file__).parent / "clickup_shots_list_template.pckl"

with open(path_config, 'r') as f:
    clickup_api = json.load(f)
#
# print(clickup_api.get('API_KEY'))
# print(clickup_api.get('JOBS_ID'))

headers = {
    'Authorization': clickup_api.get('API_KEY'),
    'Content-Type': 'application/json'
}

'''
Based on SHOW:title field change the template reading frm .pickle file
to update xxxxx (stored there) to the proper title.
Update the url to point to the Workspace.
Encode the multistring variable stored in .pickle to byte-string format (utf-8),
required by Clickup API and POST to create the Space (=Show).
Get the space_id to be written to database and for creating "folderless"
list in Clickup.
Read the multistring variable from .pickle file (for list).
Encode to utf-8.
POST to create folderless list SHOTS (same will be for ASSETS -> replace SHOTS for ASSETS in variable?).
Get the list_id to store in database.s
'''
f = open(path_clickup_space_template, 'rb')
clickup_space = pickle.load(f)
f.close()
clickup_space = clickup_space.replace('xxxxx', show_title)
url = 'https://api.clickup.com/api/v2/team/{}/space'.format(clickup_api.get('JOBS_ID'))
clickup_space = clickup_space.encode('utf-8')
request = urllib.request.Request(url, data=clickup_space, headers=headers)
response_body = urllib.request.urlopen(request, context=ssl.create_default_context(cafile=certifi.where())).read()
response_dict = json.loads(response_body)

space_id = response_dict.get('id')

f = open(path_clickup_shots_list_template, 'rb')
clickup_shots_list = pickle.load(f)
f.close()
url = 'https://api.clickup.com/api/v2/space/{}/list'.format(space_id)

clickup_shots_list = clickup_shots_list.encode('utf-8')
request = urllib.request.Request(url, data=clickup_shots_list, headers=headers)
response_body = urllib.request.urlopen(request, context=ssl.create_default_context(cafile=certifi.where())).read()
response_dict = json.loads(response_body)

list_id = response_dict.get('id')
