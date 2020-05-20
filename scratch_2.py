import pickle

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



f = open('clickup_shots_list_template.pckl', 'wb')
pickle.dump(values, f)
f.close()