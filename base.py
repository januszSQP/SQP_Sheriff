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
    username = db.Column('username', db.String(30), unique=True, nullable=False)
    icon = db.Column('icon', db.String(255))
    permissions = db.Column('permissions', db.Integer)

    tasks = db.relationship('Task', backref='User', lazy='dynamic')
    comments = db.relationship('Comment', backref='User', lazy='dynamic')

    def __repr__(self):
        return '<User: %r>' % self.username

class Show(db.Model):
    __tablename__ = 'Show'
    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column('title', db.String(30),unique=True, nullable=False)
    short = db.Column('short', db.String(8), unique=True, nullable=False)
    poster = db.Column('poster', db.String(255), unique=True)
    resolution = db.Column('resolution', db.String(10))
    fps = db.Column('fps', db.String(5))
    colorspace = db.Column('colorspace', db.String(30))
    start_date = db.Column('start_date', db.DateTime())
    clickup_space_id = db.Column('clickup_space_id', db.String(16), unique=True)
    clickup_shot_list_id = db.Column('clickup_shot_list_id', db.String(16))
    clickup_asset_list_id = db.Column('clickup_asset_list_id', db.String(16), unique=True)

    shots = db.relationship('Shot', backref='Show', lazy='dynamic')

    def __repr__(self):
        return '<Title: %r>' % self.title


class Sequence(db.Model):
    __tablename__ = 'Sequence'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(50))
    shots = db.relationship('Shot', backref='Sequence', lazy='dynamic')

    def __repr__(self):
        return '<Name: %r>' % self.name


class Shot(db.Model):
    __tablename__ = 'Shot'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(50), nullable=False)
    thumbnail = db.Column('thumbnail', db.String(255))
    resolution = db.Column('resolution', db.String(10))
    fps = db.Column('fps', db.String(5))
    start_frame = db.Column('start_frame', db.String(5))
    end_frame = db.Column('end_frame', db.String(5))
    colorspace = db.Column('colorspace', db.String(30))
    lut = db.Column('lut', db.String(255))
    camera = db.Column('camera', db.String(255))
    lens_dist = db.Column('lens_dist', db.String(255))
    start_date = db.Column('start_date', db.DateTime())

    clickup_task_id = db.Column('clickup_task_id', db.String(16), unique=True)


    show_id = db.Column('show_id', db.ForeignKey('Show.id'))
    seq_id = db.Column('seq_id', db.ForeignKey('Sequence.id'))


    tasks = db.relationship('Task', backref='Shot', lazy='dynamic')

    def __repr__(self):
        return '<Name: %r>' % self.name

class Task(db.Model):
    __tablename__ = 'Task'
    id = db.Column('id', db.Integer, primary_key=True)
    type = db.Column('type', db.Integer, nullable=False)
    status = db.Column('status', db.Integer)
    difficulty = db.Column('difficulty', db.Integer)

    shot_id = db.Column('shot_id', db.ForeignKey('Shot.id'))
    user_id = db.Column('user_id', db.ForeignKey('User.id'))

    versions = db.relationship('Version', backref='Task', lazy='dynamic')

    def __repr__(self):
        return '<Type: %r>' % self.type


class Version(db.Model):
    __tablename__ = 'Version'
    id = db.Column('id', db.Integer, primary_key=True)
    number = db.Column('number', db.Integer, nullable=False)
    type = db.Column('type', db.Integer, nullable=False)
    script_path = db.Column('script_path', db.String(255))
    render_path = db.Column('render_path', db.String(255))
    review_path = db.Column('review_path', db.String(255))
    date = db.Column('start_date', db.DateTime())
    thumbnail = db.Column('thumbnail', db.String(255))

    task_id = db.Column('task_id', db.ForeignKey('Task.id'))

    comments = db.relationship('Comment', backref='Version', lazy='dynamic')

    def __repr__(self):
        return '<Version No.: %r>' % self.number

class Comment(db.Model):
    __tablename__ = 'Comment'
    id = db.Column('id', db.Integer, primary_key=True)
    type = db.Column('type', db.Integer, nullable=False)
    text = db.Column('script_path', db.String(255))
    date = db.Column('start_date', db.DateTime())

    user_id = db.Column('user_id', db.ForeignKey('User.id'))
    version_id = db.Column('version_id', db.ForeignKey('Version.id'))

    def __repr__(self):
        return '<Comment Type: %r>' % self.type


class Element(db.Model):
    __tablename__ = 'Element'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(50), nullable=False)
    description = db.Column('description', db.String(255))
    path = db.Column('path', db.String(255))
    type = db.Column('type', db.Integer)

    def __repr__(self):
        return '<Element name: %r>' % self.name
