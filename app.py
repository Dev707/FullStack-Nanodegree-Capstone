import json
import os
import re
from flask import Flask, request, abort, jsonify, render_template
from flask_cors import CORS
from models import setup_db, Movie, Actor, db_drop_and_create_all
from auth import AuthError, requires_auth


def create_app(test_config=None):

    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    #db_drop_and_create_all()

    '''
    Set up CORS(Cross Origin Resource Sharing).
    Allow '*' for all origins.
    Delete the sample route after implementing the API endpoints
    '''

    CORS(app, resources={"/": {"origin": "*"}})

    '''
    CORS Headers. Use the after_request decorator
    to set Access-Control-Allow
    '''
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,POST,PATCH,DELETE,OPTIONS')

        return response

    @app.route('/', methods=['GET'])
    def index():
        access_token = request.form['access_token']
        return render_template("index.html", access_token=access_token)

    '''
    @Implement endpoint
    GET /actors
        it should require the 'get:actors' permission
    returns status code 200 and json {"success": True, "actors": actors}
        where actors is the list of actors
    '''

    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def get_actors(payload):
        actors = Actor.query.all()
        return jsonify({
            'success': True,
            'actors': [actor.format() for actor in actors]
        }), 200

    '''
    @Implement delete endpoint
    DELETE /actors/<id>
        where <id> is the existing actor id
        it should require the 'delete:actors' permission
    returns status code 200 and json {"success": True, "delete": id}
        where id is the id of the deleted record
    '''

    @app.route('/actors/<int:id>', methods=['DELETE'])
    @requires_auth('delete:actor')
    def delete_actor(payload, id):
        actor = Actor.query.filter(Actor.id == id).one_or_none()
        if actor:
            try:
                actor.delete()
                return jsonify({
                    'success': True,
                    'delete': id,
                })
            except BaseException:
                abort(422)
        else:
            abort(404)

    '''
    @Implement endpoint
    POST /actors
        it should require the 'post:actors' permission
    returns status code 200 and json {"success": True, "actor": actor}
        where actor is an array containing only the newly created actor
    '''

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actor')
    def add_actor(payload):
        body = request.get_json()
        new_name = body['name']
        new_age = body['age']
        actor = Actor(name=new_name, age=new_age)
        actor.insert()
        return jsonify({
            'success': True,
            'actor': actor.format()
        }), 200

    '''
    @Implement endpoint
    PATCH /actors/<id>
        where <id> is the existing actor id
        it should update the corresponding row for <id>
        it should require the 'patch:actors' permission
    returns status code 200 and json {"success": True, "actor": actor}
        where movie an array containing only the updated actor
    '''

    @app.route('/actors/<int:id>', methods=['PATCH'])
    @requires_auth('patch:actor')
    def modify_actor(payload, id):
        actor = Actor.query.filter_by(id=id).one_or_none()
        if actor is None:
            abort(404)
        body = request.get_json()
        try:
            body_name = body.get('name')
            body_age = body.get('age')
            if body_name:
                actor.name = body_name
            if body_age:
                actor.age = body_age
            actor.update()
        except Exception:
            abort(400)
        return jsonify({
            'success': True,
            'actor.id': actor.id
        }), 200

    '''
    @Implement endpoint
    GET /movies
        it should require the 'get:movies' permission
    returns status code 200 and json {"success": True, "movies": movies}
        where movies is the list of movies
    '''

    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_movies(payload):
        movies = Movie.query.all()
        return jsonify({
            'success': True,
            'movies': [movie.format() for movie in movies]
        }), 200

    '''
    @Implement endpoint
    POST /movies
        it should require the 'post:movies' permission
    returns status code 200 and json {"success": True, "movie": movie}
        where movie is an array containing only the newly created movie
    '''

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movie')
    def add_movie(payload):
        body = request.get_json()
        new_title = body['title']
        new_release_date = body['release_date']
        movie = Movie(title=new_title, release_date=new_release_date)
        movie.insert()
        return jsonify({
            'success': True,
            'movie': movie.format()
        }), 200

    '''
    @Implement endpoint
    PATCH /movies/<id>
        where <id> is the existing movie id
        it should respond with a 404 error if <id> is not found
        it should require the 'patch:movies' permission
    returns status code 200 and json {"success": True, "movie": movie}
        where movie an array containing only the updated movie
    '''

    @app.route('/movies/<int:id>', methods=['PATCH'])
    @requires_auth('patch:movie')
    def modify_movie(payload, id):
        movie = Movie.query.filter_by(id=id).one_or_none()
        if movie is None:
            abort(404)
        body = request.get_json()
        try:
            body_title = body.get('title')
            body_release_date = body.get('release_date')
            if body_title:
                movie.name = body_title
            if body_release_date:
                movie.age = body_release_date
            movie.update()

        except Exception:
            abort(400)

        return jsonify({
            'success': True,
            'movie': movie.id
        }), 200

    '''
    @Implement endpoint
    DELETE /movies/<id>
        where <id> is the existing movie id
        it should delete the corresponding row for <id>
        it should require the 'delete:movies' permission
    returns status code 200 and json {"success": True, "delete": id}
        where id is the id of the deleted record
    '''
    @app.route('/movies/<int:id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(jwt, id):
        movie = Movie.query.filter(Movie.id == id).one_or_none()
        if movie:
            try:
                movie.delete()
                return jsonify({
                    'success': True,
                    'delete': id,
                })
            except BaseException:
                abort(422)
        else:
            abort(404)

    '''
    Create error handlers for all expected errors
    including 400, 404, 422 and 500.
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
