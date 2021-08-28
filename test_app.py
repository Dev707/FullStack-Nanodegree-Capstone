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
        self.casting_assistant = os.environ['casting_assistant']
        self.casting_director = os.environ['casting_director']
        self.executive_producer = os.environ['executive_producer']
        self.database_name = "capstone_test"
        self.database_path = os.environ['DATABASE_URL']
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

# -------------------------------------------------------------------------------------------------

    def test_api_call_without_token(self):

        response = self.client().get('/actors')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 401)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unauthorized")

    '''
    RBAC test
    '''

    def test_insert_movie_with_unauthorized_token_permission(self):
        movie_dict = {

            'title': 'The Matrix 4',
            'release_date': '2022-12-12'
        }

        response = self.client().post('/movies',
                                      headers={'Authorization': "Bearer {}".
                                               format(self.casting_assistant)},
                                      json=movie_dict)

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unauthorized')

    def test_delete_actor_with_unautorized_token_permission(self):

        response = self.client().delete('/actors/1',
                                        headers={'Authorization': "Bearer {}".
                                                 format(self.casting_assistant)
                                                 })

        deleted_actor = Actor.query.filter_by(id=1).one_or_none()

        self.assertEqual(response.status_code, 401)

    '''
    Success Behavior Actors End Points
    '''

    def test_get_all_actors(self):

        response = self.client().get(
            '/actors',
            headers={'Authorization': "Bearer {}"
                     .format(self.casting_assistant)
                     })

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_insert_actor(self):

        actor_dict = {

            'name': 'Will Smith',
            'age': 49
        }

        response = self.client().post('/actors', headers={
            'Authorization': "Bearer {}"
            .format(self.casting_director)}, json=actor_dict)

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(data['success'], True)

    def test_edit_actor(self):

        response = self.client().patch('/actors/1',
                                       headers={'Authorization': "Bearer {}".
                                                format(self.casting_director)
                                                }, json={'name': 'Neo Martin'}
                                       )
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    def error_404_test_edit_actor(self):

        response = self.client().patch('/actors/999',
                                       headers={'Authorization': "Bearer {}".
                                                format(self.casting_director)
                                                }, json={'name': 'Neo Martin'}
                                       )
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)

    def test_delete_actor(self):

        response = self.client().delete('/actors/1',
                                        headers={'Authorization': "Bearer {}".
                                                 format(self.casting_director)
                                                 })

        deleted_actor = Actor.query.filter_by(id=1).one_or_none()

        self.assertEqual(response.status_code, 200)

        self.assertEqual(deleted_actor, None)

    def error_404_test_delete_actor(self):

        response = self.client().delete('/actors/999',
                                        headers={'Authorization': "Bearer {}".
                                                 format(self.casting_director)
                                                 })

        deleted_actor = Actor.query.filter_by(id=999).one_or_none()

        self.assertEqual(response.status_code, 404)

# -------------------------------------------------------------------------------------------------

    def test_get_all_movies(self):

        response = self.client().get(
            '/movies', headers={'Authorization': "Bearer {}".
                                format(self.casting_assistant)
                                })

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_insert_movie(self):
        movie_dict = {

            'title': 'The Matrix 4',
            'release_date': '2022-12-12'
        }

        response = self.client().post('/movies', headers={
            'Authorization': "Bearer {}".
            format(self.executive_producer)},
            json=movie_dict)

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_edit_movie(self):

        response = self.client().patch('/movies/1',
                                       headers={
                                           'Authorization': "Bearer {}".
                                           format(self.casting_director)},
                                       json={'title': 'interstellar 2'})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    def error_404_test_edit_movie(self):

        response = self.client().patch('/movies/999',
                                       headers={
                                           'Authorization': "Bearer {}".
                                           format(self.casting_director)},
                                       json={'title': 'interstellar 2'})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)

    def test_delete_movie(self):

        response = self.client().delete('/movies/1', headers={
            'Authorization': "Bearer {}".format(self.executive_producer)})

        deleted_movie = Movie.query.filter_by(id=1).one_or_none()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(deleted_movie, None)

    def error_404_test_delete_movie(self):

        response = self.client().delete('/movies/999', headers={
            'Authorization': "Bearer {}".format(self.executive_producer)})

        deleted_movie = Movie.query.filter_by(id=999).one_or_none()

        self.assertEqual(response.status_code, 404)


# -------------------------------------------------------------------------------------------------


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
