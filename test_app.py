import os
import sys
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, '..')

from app import create_app
from models import setup_db, Actor, Movie, db_drop_and_create_all


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

    #reset database:
    db_drop_and_create_all()
    
    def tearDown(self):
        pass

    '''
    From a total of 17 tests is to be expected 8 Error tests
    '''

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

    #ERROR Test: this test should fail
    def test_401_get_actors(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    #this test should pass
    def test_get_movies(self):
        res = self.client().get('movies',
                                headers={'Authorization': 'Bearer ' + self.assistent})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    #ERROR Test: following test should fail
    def test_401_get_movies(self):
        res = self.client().get('/movies',
                                headers={})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

#DELETE Endpoints:

    #following test should pass
    def test_delete_actor(self):
        res = self.client().delete('/actors/1',
                                    headers={'Authorization': 'Bearer ' + self.producer})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted'])

    #ERROR Test: following test should fail
    def test_401_delete_actor(self):
        res = self.client().delete('/actors/1',
                            headers={'Authorization': 'Bearer ' + self.assistent})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    #following test should pass
    def test_delete_movie(self):
        res = self.client().delete('movies/1',
                                    headers={'Authorization': 'Bearer ' + self.producer})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted'])

    #ERROR Test: following test should fail
    def test_401_delete_movie(self):
        res = self.client().delete('movies/1',
                                    headers={'Authorization': 'Bearer ' + self.assistent})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
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
    
    #ERROR Test: following test should fail
    def test_401_create_actor(self):
        res = self.client().post('/actors',
                                headers={'Authorization': 'Bearer ' + self.assistent},
                                json={'age': 20})
        
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
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

    #ERORR Test: following test should fail
    def test_401_create_movie(self):
        res = self.client().post('/movies',
                                    headers={'Authorization': 'Bearer ' + self.assistent},
                                    json={'release_date': '1991'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

#PATCH Endpoints

    #following test should pass
    def test_update_actor(self):
        res = self.client().patch('/actors/1',
                                    headers={'Authorization': 'Bearer ' + self.producer},
                                    json={'name': 'John Test'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])

    #ERROR TEST: following test should fail

    def test_401_update_actor(self):
        res = self.client().patch('/actors/1',
                                    headers={'Authorization': 'Bearer ' + self.assistent},
                                    json={'name': 'John'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    #following test should pass
    def test_update_movie(self):
        res = self.client().patch('/movies/1',
                                    headers={'Authorization': 'Bearer ' + self.producer},
                                    json={'title': 'update test'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])

    #ERROR TEST: following test should fail
    def test_401_update_movie(self):
        res = self.client().patch('/movies/1',
                                    headers={'Authorization': 'Bearer ' + self.assistent},
                                    json={'release_date': '2001'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

if __name__ == '__main__':
    unittest.main()