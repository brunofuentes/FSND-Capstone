import os
import sys
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, '..')

from app.app import create_app
from app.models import setup_db, Actor, Movie


class CastingAgencyTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client

        self.assistent = os.environ('ASSISTENT')
        self.director = os.environ('DIRECTOR')
        self.producer = os.environ('PRODUCER')

        self.database_path = os.environ['DATABASE_URL']
        # self.database_path = 'postgresql://Bruno@localhost:5432/capstone'
        setup_db(self.app, self.database_path)

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

    # creates a new actor

        self.new_actor = {
            'id': 69,
            'name': 'test01',
            'gender': 'test01'
        }

    #creates a new movie

        self.new_movie = {
            'id': 69,
            'title': 'test01',
            'release_date': '1991'
        }
    
    def tearDown(self):
        pass

    # TESTS FOR ACTORS
    # Test listing actors

    #testing with assistent token, should pass

    def test_retrieve_actors(self):
        res = self.client().get('/actors',
                                headers={'Authorization': 'Bearer' + self.assistent})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])
        self.assertTrue(data['total_actors'])

    #following test should fail (no token provided)

    def test_401_retrieve_actors_NoAuth(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)

    # Test creating actors

    #testing with producer token, test should pass

    def test_create_actor(self):
        res = self.client().post('/actors',
                                headers={'Authorization': 'Bearer ' + self.producer},
                                json={'name': 'John'})
        
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created actor'])
    
    #following test should fail, no actor-name given

    def test_400_create_actor(self):
        res = self.client().post('/actor',
                                headers={'Authorization': 'Bearer ' + self.producer},
                                json={'age': 20})
        
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Bad request')

    # Test editing actors

    #testing with producer token, test should pass

    def test_update_actor(self):
        res = self.client().patch('/actors/2',
                                    headers={'Authorization': 'Bearer ' + self.producer},
                                    json={'name': 'John'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])

    #following test should fail, no actor-name given

    def test_400_patch_actor(self):
        res = self.client().patch('/actors/2',
                                    headers={'Authorization': 'Bearer ' + self.producer},
                                    json={'age': 20})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Bad request')

    #Test deleting actors

    #testing with producer token, test should pass
    def test_delete_actor(self):
        res = self.client().delete('/actors/2',
                                    headers={'Authorization': 'Bearer ' + self.producer})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted'])

    #testing with assistent token, test should fail

    def test_401_delete_actor(self):
        res = self.client('/actors/2',
                            headers={'Authorization': 'Bearer ' + self.assistent})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    #TESTS FOR MOVIES
    # Test listing movies

    #following test should pass, with a token from a casting assistent
    def test_retrieve_movies(self):
        res = self.client().get('/movies',
                                headers={'Authorization': 'Bearer ' + self.assistent})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['movies'])

    #following test should fail, no token from assistent
    def test_401_list_movies_NoAuth(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    #Test creating movies

    #testing with producer token, test should pass

    def test_create_movie(self):
        res = self.client().post('/movies',
                                    headers={'Authorization': 'Bearer ' + self.producer},
                                    json={'title': 'Testing01'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created movie'])

    #following test should fail, no actor-name is given
    def test_400_create_movie(self):
        res = self.client().post('/movies',
                                    headers={'Authorization': 'Bearer ' + self.producer},
                                    json={'release_date': 1991})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], 'Bad request')

    #Test editing movies

    #testing with producer token, test should pass

    def test_update_movie(self):
        res = self.client().patch('/movies/2',
                                    headers={'Authorization': 'Bearer ' + self.producer},
                                    json={'title': 'CLICK', 'release_date': '2001'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])

    #following test should fail, no movie-name is given

    def test_400_update_movie(self):
        res = self.client().patch('/movies/2',
                                    headers={'Authorization': 'Bearer ' + self.producer},
                                    json={'release_date': '2001'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['message'], 'Bad request')

    #Testing delete movies

    #testing with producer token, test should pass
    def test_delete_movie(self):
        res = self.client().delete('movies/3',
                                    headers={'Authorization': 'Bearer ' + self.producer})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted'])

    #following test should fail, token from assistent used

    def test_404_delete_movie(self):
        res = self.client().delete('/movies/1',
                                    headers={'Authorization': 'Bearer ' + self.assistent})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

if __name__ == '__main__':
    unittest.main()