import json
import os
import re
from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from models import setup_db, Movie, Actor
from auth import AuthError, requires_auth


def create_app(test_config=None):

    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    # allow resource sharing in all domain parts
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    @app.after_request
    def after_request(response):

        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,POST,PATCH,DELETE,OPTIONS')

        return response

    '''
    GET Actors endpoint
    Fetch all actrors from database
    '''
    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def get_actors(payload):
        # fetch data from database
        actors = Actor.query.all()
        # return json response
        return jsonify({
            'success': True,
            'actors': [actor.format() for actor in actors]
        }), 200

    '''
    DELETE Actor endpoint
    delete an actor from endpoint with given id
    '''
    @app.route('/actors/<int:id>', methods=['DELETE'])
    @requires_auth('delete:actor')
    def delete_actor(payload, id):
        # fetch data from db
        actor = Actor.query.filter_by(id=id).one_or_none()
        # check if there is any data fetched from db
        if actor is None:
            abort(404)
        # delete actor from db
        actor.delete()
        # return json response
        return jsonify({
            'success': True,
            'actor_id': actor.format()
        }), 200

    '''
    POST Actor Endpoint
    Create an actor and store it in db
    '''
    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actor')
    def add_actor(payload):

        # fetch raw data
        body = request.get_json()

        new_name = body['name']
        new_age = body['age']

        # create an object with fetched data from body and insert it to db
        actor = Actor(name=new_name, age=new_age)
        actor.insert()
        # return json response
        return jsonify({
            'success': True,
            'actor': actor.format()
        }), 200

    '''
    PATCH Actors endpoint
    Edit Actors from db with given id
    '''
    @app.route('/actors/<int:id>', methods=['PATCH'])
    @requires_auth('patch:actor')
    def modify_actor(payload, id):

        # Check if the record is available in db with given id
        actor = Actor.query.filter_by(id=id).one_or_none()

        # Check the record is not none
        if actor is None:
            abort(404)
        # fetch raw data
        body = request.get_json()

        try:

            body_name = body.get('name')
            body_age = body.get('age')
            # if body_name is not Null update the record in db
            if body_name:
                actor.name = body_name
            # if body_age is not Null update the record in db
            if body_age:
                actor.age = body_age

            actor.update()

        except Exception:
            abort(400)

        # return json response
        return jsonify({

            'success': True,
            'actor.id': actor.id

        }), 200
    '''
    GET movies endpoint
    Fetches data from db
    '''
    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_movies(payload):
        # fetch data from db
        movies = Movie.query.all()
        # return json response with fetched data from db
        return jsonify({
            'success': True,
            'movies': [movie.format() for movie in movies]
        }), 200

    '''
    DELETE movie endpoint
    Delete record form db with given id
    '''
    @app.route('/movies/<int:id>', methods=['DELETE'])
    def delete_movie(id):
        # search for movie
        movie = Movie.query.filter_by(id=id).one_or_none()
        # if movie not found from db abort 404
        if movie is None:
            abort(404)

        # if the given id was in db , delete it from db
        movie.delete()
        # return json response
        return jsonify({
            'success': True,
            'movie': movie.format()
        }), 200

    '''
    POST movies
    Allow you to create a movie and then stores it in db
    '''

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movie')
    def add_movie(payload):
        # fetch raw data
        body = request.get_json()

        new_title = body['title']
        new_release_date = body['release_date']
        # create a new object from raw data
        movie = Movie(title=new_title, release_date=new_release_date)
        # insert the object in db
        movie.insert()
        # return json response
        return jsonify({
            'success': True,
            'movie': movie.format()
        }), 200
    '''
    PATCH Movie
    Allow you to change fields in DB
    '''
    @app.route('/movies/<int:id>', methods=['PATCH'])
    @requires_auth('patch:movie')
    def modify_movie(payload, id):
        # search in db by the given id
        movie = Movie.query.filter_by(id=id).one_or_none()

        # check if the movie is in the db
        if movie is None:
            abort(404)
        # fetch raw data
        body = request.get_json()

        try:

            body_title = body.get('title')
            body_release_date = body.get('release_date')
            # if title was changed from front update the db with the new value
            if body_title:
                movie.name = body_title
            # if release_date was from front update the db with new value
            if body_release_date:
                movie.age = body_release_date
            # commit updates
            movie.update()

        except Exception:
            abort(400)

        # return json response
        return jsonify({

            'success': True,
            'movie.id': movie.id

        }), 200

    '''
  Error Handler

  '''

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(404)
    def resource_not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'resource not found'
        }), 404

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            'success': False,
            'error': 401,
            'message': 'unauthorized'

        }), 401

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
