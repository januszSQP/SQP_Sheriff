import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import date
import sqlalchemy
import mysql.connector

import base

current_show = 'SKYSCRAPER_TEASER'

def TestList():
    show = base.Show.query.filter(base.Show.title == current_show).first()
    res = show.resolution
    fps = show.fps
    #
    # new_shot = Shot(name='0020', resolution = res, fps = fps, start_frame = '1001', end_frame = '1075',
    #                 clickup_task_id = '54n2c2', clickup_list_id = '19408057', show_id=show.id)
    # #
    shots = base.Shot.query.filter(base.Shot.show_id == show.id)
    for shot in shots:
        print(shot.name)

    return "Please list"

lst = TestList()

print(lst)