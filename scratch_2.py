'''

    SCRATCH FILE FOR CREATING PICKLE FILES TO STORE
    VARIABLES.
    CONTENT MAY BE CHANGED WHEN NEEDED.

'''

import pickle

'''
    SETUP FILENAME BELOW
'''
filename = 'name_here' + '.pckl'


'''
    SETUP THE VARIABLE BELOW
'''
values = """
  {
    "name": "SHOTS",
    "content": "Shots List",
    "due_date": 1567780450202,
    "due_date_time": false,
    "priority": 3,
    "assignee": 0,
    "status": "blue"
  }
"""

'''
    RUN THE CODE
'''

f = open(filename, 'wb')
pickle.dump(values, f)
f.close()