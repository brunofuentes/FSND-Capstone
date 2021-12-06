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

        self.database_path = os.environ['DATABASE_URL']

        self.assistent = os.getenv('ASSISTENT')
        self.director = os.getenv('DIRECTOR')
        self.producer = os.getenv('PRODUCER')

        # self.database_path = 'postgresql://Bruno@localhost:5432/capstone'
        setup_db(self.app, self.database_path)

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

    #creates a new actor

        self.actor = {
            'name': 'actor_testing',
            'age': 29,
            'gender': 'test01'
        }
        print('New Actor created')

    #creates a new movie

        self.movie = {
            'title': 'movie_testing',
            'release_date': '1991'
        }
        print('New Movie created')
    
    def tearDown(self):
        pass


#General Test - Server status

    def test_server_status(self):
        res = self.client().get('/')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


#GET Endpoints:

    #this test should pass
    def test_get_actors(self):
        res = self.client().get('/actors',
                                headers={'Authorization': 'Bearer ' + self.assistent})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    #this test should fail
    def test_401_get_actors(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)

    #this test should pass
    def test_get_movies(self):
        res = self.client().get('movies',
                                headers={'Authorization': 'Bearer ' + self.assistent})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    #following test should fail
    def test_401_get_movies(self):
        res = self.client().get('/movies',
                                headers={})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

#DELETE Endpoints:

    #following test should pass
    # def test_delete_actor(self):
    #     res = self.client().delete('/actors/5',
    #                                 headers={'Authorization': 'Bearer ' + self.producer})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['deleted'])

    #following test should fail
    def test_403_delete_actor(self):
        res = self.client().delete('/actors/1',
                            headers={'Authorization': 'Bearer ' + self.assistent})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)

    #following test should pass
    # def test_delete_movie(self):
    #     res = self.client().delete('movies/8',
    #                                 headers={'Authorization': 'Bearer ' + self.producer})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['deleted'])

    #following test should fail
    def test_403_delete_movie(self):
        res = self.client().delete('movies/8',
                                    headers={'Authorization': 'Bearer ' + self.assistent})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)

#POST Endpoints:

    #following test should pass
    def test_create_actor(self):
        res = self.client().post('/actors',
                                headers={'Authorization': 'Bearer ' + self.producer},
                                json={'name': 'John'})
        
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created actor'])
    
    #following test should fail
    def test_403_create_actor(self):
        res = self.client().post('/actors',
                                headers={'Authorization': 'Bearer ' + self.assistent},
                                json={'age': 20})
        
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)

    #following test should pass
    def test_create_movie(self):
        res = self.client().post('/movies',
                                    headers={'Authorization': 'Bearer ' + self.producer},
                                    json={'title': 'Testing01'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created movie'])

    #following test should fail, no actor-name is given
    def test_403_create_movie(self):
        res = self.client().post('/movies',
                                    headers={'Authorization': 'Bearer ' + self.assistent},
                                    json={'release_date': 1991})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)

#PATCH Endpoints

    #following test should pass
    def test_update_actor(self):
        res = self.client().patch('/actors/4',
                                    headers={'Authorization': 'Bearer ' + self.producer},
                                    json={'name': 'John Test'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])

    #following test should fail

    def test_403_update_actor(self):
        res = self.client().patch('/actors/2',
                                    headers={'Authorization': 'Bearer ' + self.assistent},
                                    json={'name': 'John'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)

    #following test should pass
    def test_update_movie(self):
        res = self.client().patch('/movies/3',
                                    headers={'Authorization': 'Bearer ' + self.producer},
                                    json={'title': 'CLICK', 'release_date': '2001'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])

    #following test should fail
    def test_403_update_movie(self):
        res = self.client().patch('/movies/4',
                                    headers={'Authorization': 'Bearer ' + self.producer},
                                    json={'release_date': '2001'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)

if __name__ == '__main__':
    unittest.main()