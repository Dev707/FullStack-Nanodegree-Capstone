import os
import unittest
import json
from flask.wrappers import Response
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Actor, Movie


class CapstoneTestCase(unittest.TestCase):
    """This class represents the Capstone test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        #self.DB_HOST = os.getenv('DB_HOST', 'localhost:5432')
        #self.DB_USER = os.getenv('DB_USER', 'postgres')
        #self.DB_PASSWORD = os.getenv('DB_PASSWORD', 'admin')
        #self.DB_NAME = os.getenv('DB_NAME', 'capstone_test')
        #self.database_path = 'postgresql://{}:{}@{}/{}'.format(
        #    self.DB_USER, self.DB_PASSWORD, self.DB_HOST, self.DB_NAME)
        self.database_path = os.environ['DATABASE_URL']
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    casting_assistant = format(os.environ.get('casting_assistant'))
    casting_director = format(os.environ.get('casting_director'))
    executive_producer = format(os.environ.get('executive_producer'))

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation
    and for expected errors.
    """

    '''
    test api without token
    '''

    def test_api_without_token(self):

        response = self.client().get('/actors')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 401)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unauthorized")

    '''
    RBAC test
    '''

    def test_to_insert_new_movie_without_permission(self):
        movie_dict = {

            'title': 'Tom and Jerry',
            'release_date': '2021-11-15'
        }

        response = self.client().post('/movies',
                                      headers={'Authorization': "Bearer {}".
                                               format(self.casting_assistant)},
                                      json=movie_dict)

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unauthorized')

    def test_to_delete_actor_without_permission(self):

        response = self.client().delete('/actors/1',
                                        headers={'Authorization': "Bearer {}".
                                                 format(self.casting_assistant)
                                                 })

        deleted_actor = Actor.query.filter_by(id=1).one_or_none()

        self.assertEqual(response.status_code, 401)

    '''
    Success Behavior Actors End Points
    '''
    def test_to_insert_new_actor(self):

        actor_dict = {

            'name': 'Mjeed jerry',
            'age': 12
        }

        response = self.client().post('/actors', headers={
            'Authorization': "Bearer {}"
            .format(self.casting_director)}, json=actor_dict)

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(data['success'], True)

    def test_to_edit_actor(self):

        response = self.client().patch('/actors/1',
                                       headers={'Authorization': "Bearer {}".
                                                format(self.casting_director)
                                                }, json={'name': 'Mr Khalid'}
                                       )
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_to_get_all_actors(self):

        response = self.client().get(
            '/actors',
            headers={'Authorization': "Bearer {}"
                     .format(self.casting_assistant)
                     })

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_edit_actor_not_exiest(self):

        response = self.client().patch('/actors/222',
                                       headers={'Authorization': "Bearer {}".
                                                format(self.casting_director)
                                                }, json={'name': 'Mr Khalid'}
                                       )
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)

    def test_to_delete_actor(self):

        response = self.client().delete('/actors/1',
                                        headers={'Authorization': "Bearer {}".
                                                 format(self.casting_director)
                                                 })

        deleted_actor = Actor.query.filter_by(id=1).one_or_none()

        self.assertEqual(response.status_code, 200)

        self.assertEqual(deleted_actor, None)

    def error_404_test_delete_actor(self):

        response = self.client().delete('/actors/222',
                                        headers={'Authorization': "Bearer {}".
                                                 format(self.casting_director)
                                                 })

        deleted_actor = Actor.query.filter_by(id=222).one_or_none()

        self.assertEqual(response.status_code, 404)

    """
    Test API endpoint for movies
    """
    def test_to_insert_movie(self):
        movie_dict = {

            'title': 'FCIT 2021',
            'release_date': '2021-08-28'
        }

        response = self.client().post('/movies', headers={
            'Authorization': "Bearer {}".
            format(self.executive_producer)},
            json=movie_dict)

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_to_get_all_movies(self):

        response = self.client().get(
            '/movies', headers={'Authorization': "Bearer {}".
                                format(self.casting_assistant)
                                })

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_to_edit_movie_not_exiest(self):

        response = self.client().patch('/movies/999',
                                       headers={
                                           'Authorization': "Bearer {}".
                                           format(self.casting_director)},
                                       json={'title': 'hola mola'})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)

    def test_to_delete_movie(self):

        response = self.client().delete('/movies/1', headers={
            'Authorization': "Bearer {}".format(self.executive_producer)})

        deleted_movie = Movie.query.filter_by(id=1).one_or_none()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(deleted_movie, None)

    def test_edit_movie(self):

        response = self.client().patch('/movies/1',
                                       headers={
                                           'Authorization': "Bearer {}".
                                           format(self.casting_director)},
                                       json={'title': 'hola mola'})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
    def error_404_test_delete_movie(self):

        response = self.client().delete('/movies/222', headers={
            'Authorization': "Bearer {}".format(self.executive_producer)})

        deleted_movie = Movie.query.filter_by(id=222).one_or_none()

        self.assertEqual(response.status_code, 404)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
