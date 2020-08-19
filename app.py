import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json

from models import setup_db, Movie, Actor
from auth import AuthError, requires_auth

#https://dcadventuresonline.us.auth0.com/authorize?audience=capstone&response_type=token&client_id=efycj8gd3uVhe6Uu3ejqSl1q50Yu2dRc&redirect_uri=https://mikewycklendtfcapstone.herokuapp.com/calback

app = Flask(__name__)
setup_db(app)

@app.route('/')
def index():
  return 'Hello World'

@app.route('/movies')
@requires_auth('get:movies')
def movies(payload):
  try:
    movies = Movie.query.all()
    movie_info = [movies.format() for movie in movies]

    return jsonify({
      'status_code': 200,
      'success': True,
      'movies': movie_info
    })

  except:
    abort(400)

@app.route('/actors')
@requires_auth('get:actors')
def actors(payload):
  try:
    actors = Actor.query.all()
    actor_info = [actors.format() for actor in actors]

    return jsonify({
      'status_code': 200,
      'success': True,
      'actors': actor_info
    })

  except:
    abort(400)

@app.route('/actors/<int:id>', methods=['DELETE'])
@requires_auth('delete:actors')
def delete_actor(payload, id):
  try:
    actor = Actor.query.filter(Actor.id==id).one_or_none()
    actor.delete()
    return jsonify({'success': True})
  except:
    abort(422)

@app.route('/movies/<int:id>', methods=['DELETE'])
@requires_auth('delete:movies')
def delete_movie(payload, id):
  try:
    movie = Movie.query.filter(Movie.id==id).one_or_none()
    movie.delete()
    return jsonify({'success': True})
  except:
    abort(422)

@app.route('/movies', methods=['POST'])
@requires_auth('post:movies')
def add_movie(payload):
  try:
    body = request.get_json()
    title = body['title']
    release = body['release']
    
    movie = Movie(title=title, release=release)
    movie.insert()
    
    movie_formatted = movie.format()
    
    return jsonify({
      'status_code': 200,
      'success': True,
      'movie': movie_formatted
    })
  except:
    abort(422)

@app.route('/actors', methods=['POST'])
@requires_auth('post:actors')
def add_actor(payload):
  try:
    body = request.get_json()
    name = body['name']
    age = body['age']
    gender = body['gender']
    actor = Actor(name=name, age=age, gender=gender)
    actor.insert()
    actor_formatted = actor.format()
    return jsonify({
      'status_code': 200,
      'success': True,
      'actor': actor_formatted
      })
  except:
    abort(422)

@app.route('/movies/<int:id>', methods=['PATCH'])
@requires_auth('patch:movies')
def edit_movie(payload, id):
  try:
    body = request.get_json()
    title = body['title', None]
    release = body['release', None]

    movie = Movie.query.filter(Movie.id == id).one()
    movie.title = title
    movie.release = release

    movie_formatted = movie.format()

    return jsonify({
      'status_code': 200,
      'success': True,
      'movie': movie_formatted
    })

  except:
    abort(422)

@app.route('/actors/<int:id>', methods=['PATCH'])
@requires_auth('patch:actors')
def edit_actor(payload, id):
  try:
    body = request.get_json()
    name = body['name', None]
    age = body['age', None]
    gender = body['gender', None]

    actor = Actor.query.filter(Actor.id == id).one()
    actor.name = name
    actor.age = age
    actor.gender = gender

    actor_formatted = actor.format()

    return jsonify({
      'status_code': 200,
      'success': True,
      'actor': actor_formatted
    })

  except:
    abort(422)

@app.route('/login')
def login():
  return 'login'

@app.route('/calback')
def callback():
  return 'callback'

@app.errorhandler(AuthError)
def handle_auth_error(ex):
  response = jsonify(ex.error)
  response.status_code = ex.status_code
  return response

if __name__ == '__main__':
  app.debug = True
  app.run(host='0.0.0.0', port=80)