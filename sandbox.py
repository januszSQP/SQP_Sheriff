import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import date
import sqlalchemy
import mysql.connector

# import config

# def gen_connection_string():
#     # if not on Google then use local MySQL
#     # if not os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
#     #     return 'mysql://root@localhost/blog'
#     # else:
#     # conn_name = 'omega-pattern-242522:europe-west1:sqp-mysql'
#     conn_name = 'omega-pattern-242522:europe-west1:sqp-mysql'
#     sql_user = 'janusz'
#     sql_pass = 'Valhala90'
#     conn_template = 'mysql+pymysql://%s:%s@/sheriff_db?unix_socket=/cloudsql/%s'
#     return conn_template % (sql_user, sql_pass, conn_name)
#
#mysql://doadmin:qxw7gzta4gfy1ibd@sqp-database-cluster-do-user-7469152-0.a.db.ondigitalocean.com:25060/defaultdb?ssl-mode=REQUIRED
app = Flask(__name__)
app.config.from_pyfile('config.cfg')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://janusz:vx1fqct7bha37y2l@sqp-database-cluster-do-user-7469152-0.a.db.ondigitalocean.com:25060/sheriff-db?charset=utf8mb4'
db = SQLAlchemy(app)


# class Test(db.Model):
#     id = db.Column(db.Integer, primary_key=True)


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
#
#
#

# show_TEST = Show(title='TEST', short='TST', resolution='2048x1536', fps='24', colorspace='ACES', start_date=date.today(), clickup_space_id = '2597557')
# show_SKYSCR = Show(title='SKYSCRAPER_TEASER', short='SKYSCR', resolution='1920x817', fps='25', colorspace='Linear RGB',
#                    start_date=date(2020, 4, 19), clickup_space_id = '2668736')



current_show = 'SKYSCRAPER_TEASER'

#
show = Show.query.filter(Show.title == current_show).first()
res = show.resolution
fps = show.fps
#
# new_shot = Shot(name='0020', resolution = res, fps = fps, start_frame = '1001', end_frame = '1075',
#                 clickup_task_id = '54n2c2', clickup_list_id = '19408057', show_id=show.id)
# #
shots = Shot.query.filter(Shot.show_id==show.id)
for shot in shots:
    print(shot.name)

# db.create_all()
#

# db.session.add(show_TEST)
# db.session.add(new_shot)
# db.session.commit()
# if __name__ == '__main__':
#     app.run()