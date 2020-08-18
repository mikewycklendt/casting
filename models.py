import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

database_name = "casting"
#database_path = 'postgresql+psycopg2://postgres:postgres@3.134.26.61:5432/casting'
database_path = 'postgres://uoflwfsmtzakue:398158105d9a64abf29451e7251b627dc580b0f9c762a562ecbe8973b0106d0e@ec2-52-72-221-20.compute-1.amazonaws.com:5432/da8qfn6n71hnkf'

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

'''
Question

'''
class Movie(db.Model):  
  __tablename__ = 'movies'

  id = Column(Integer, primary_key=True, autoincrement=True)
  title = Column(String)
  release = Column(String)

  def __init__(self, title, release):
    self.title = title
    self.release = release

  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'title': self.title,
      'release': self.release
    }

'''
Category

'''
class Actor(db.Model):  
  __tablename__ = 'actors'

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String)
  age = Column(String)
  gender = Column(String)

  def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender

  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'age': self.age,
      'gender': self.gender
    }