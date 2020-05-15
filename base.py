# coding=utf-8

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import date
import sqlalchemy
import mysql.connector

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'User'
    id = db.Column('id', db.Integer, primary_key=True)
    username = db.Column('username', db.String(25), unique=True, nullable=False)
    icon = db.Column('icon', db.String(60))
    permissions = db.Column('permissions', db.Integer)

    def __repr__(self):
        return '<User: %r>' % self.username

class Show(db.Model):
    __tablename__ = 'Show'
    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column('title', db.String(25),unique=True, nullable=False)
    short = db.Column('short', db.String(8), unique=True, nullable=False)
    poster = db.Column('poster', db.String(60), unique=True)
    resolution = db.Column('resolution', db.String(10))
    fps = db.Column('fps', db.String(5))
    colorspace = db.Column('colorspace', db.String(20))
    start_date = db.Column('start_date', db.DateTime())
    clickup_space_id = db.Column('clickup_space_id', db.String(16), unique=True)
    clickup_assets_list_id = db.Column('clickup_assets_list_id', db.String(16), unique=True)

    shots = db.relationship('Shot', backref='Show', lazy='dynamic')

    def __repr__(self):
        return '<Title: %r>' % self.title


class Sequence(db.Model):
    __tablename__ = 'Sequence'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(25))
    shots = db.relationship('Shot', backref='Sequence', lazy='dynamic')

    def __repr__(self):
        return '<Name: %r>' % self.name


class Shot(db.Model):
    __tablename__ = 'Shot'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(25), nullable=False)
    thumbnail = db.Column('thumbnail', db.String(60))
    resolution = db.Column('resolution', db.String(10))
    fps = db.Column('fps', db.String(5))
    start_frame = db.Column('start_frame', db.String(5))
    end_frame = db.Column('end_frame', db.String(5))
    colorspace = db.Column('colorspace', db.String(20))
    lut = db.Column('lut', db.String(60))
    camera = db.Column('camera', db.String(60))
    lens_dist = db.Column('lens_dist', db.String(60))
    start_date = db.Column('start_date', db.DateTime())

    clickup_task_id = db.Column('clickup_task_id', db.String(16), unique=True)
    clickup_list_id = db.Column('clickup_list_id', db.String(16))

    show_id = db.Column('show_id', db.ForeignKey('Show.id'))
    seq_id = db.Column('seq_id', db.ForeignKey('Sequence.id'))


    def __repr__(self):
        return '<Name: %r>' % self.name