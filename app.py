import os
from sys import getwindowsversion
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from models import setup_db, Movie, Actor


def create_app(test_config=None):
  # create and configure the app
	app = Flask(__name__)
	setup_db(app)

	#Cors to allow '*' for origins.
	CORS(app, resources=r'/api/*')

	#CORS Headers
	@app.after_request
	def after_request(response):
		response.headers.add(
		"Access-Control-Allow-Headers",
		"Content-Type, Authorization, true")

		response.headers.add(
		"Access-Control-Allow-Methods",
		"GET,PUT,POST,DELETE,OPTIONS")

		return response


	'''
	Endpoints:
	- GET /actors and /movies
	- DELETE /actors/ and /movies/
	- POST /actors and /movies and
	- PATCH /actors/ and /movies/
	'''

	@app.route('/actors', methods=['GET'])
	def get_actors():
		
		actors = Actor.query.order_by(Actor.id).all()

		if len(actors) == 0:
			abort(404)

		return jsonify({
			'success': True,
			'actors': actors.format() #not sure about it here !!
		})

	@app.route('/movies', methods=['GET'])
	def get_movies():
	
		movies = Movie.query.order_by(Movie.id).all()

		if len(movies) == 0:
			abort(404)

		return jsonify({
			'success': True,
			'movies': movies.format()
		})
	
	'''
	Endpoints:
	- DELETE /actors/ and /movies/
	'''

	@app.route('/actors/<int:actor_id>', methods=['DELETE'])
	def delete_actor(actor_id):

		try:

			actor = Actor.query.filter(Actor.id == actor_id).one_or_none()

			if actor is None:
				abort(404)

			else:
				actor.delete()

			return jsonify({
				'success': True,
				'deleted': actor.format()
			}), 200

		except Exception as error:
			print(error)
			abort(422)

	@app.route('/movies/<int:movie_id>', methods=['DELETE'])
	def delete_movie(movie_id):

		try:

			movie = Movie.query.filter(Movie.id == movie_id).one_or_more()

			if movie is None:
				abort(404)

			else:
				movie.delete()

			return jsonify({
				'success': True,
				'deleted': movie.format()
			}), 200

		except Exception as error:
			print(error)
			abort(422)

	'''
	Endpoints:
	- POST /actors and /movies and
	- PATCH /actors/ and /movies/
	'''

	@app.route('/actors', methods=['POST'])
	def create_actor():

		body = request.form
		new_name = body.get('name')
		new_age = body.get('age')
		new_gender = body.get('gender')

		try:
			actor = Actor(
				name = new_name,
				age = new_age,
				gender = new_gender
			)
			actor.insert()

			return jsonify({
				'success': True,
				'created actor': actor.format()
			})

		except Exception as error:
			print(error)
			abort(422)

	@app.route('/movies', methods=['POST'])
	def create_movie():

		body = request.form
		new_title = body.get('title')
		new_release_date = body.get('release_date')

		try:
			movie = Movie(
				title = new_title,
				release_date = new_release_date
			)
			movie.insert()

			return jsonify({
				'success': True,
				'created movie': movie.format()
			})

		except Exception as error:
			print(error)
			abort(422)

	'''
	Endpoints:
	- POST /actors and /movies and
	- PATCH /actors/ and /movies/
	'''

	@app.route('/actors/<int:id>', methods=['PATCH'])
	def update_actor(id):

		body = request.form
		new_name = body.get('name')
		new_age = body.get('age')
		new_gender = body.ger('gender')

		try:
			actor = Actor.query.filter(Actor.id == id).one_or_more()

			if actor is None:
				abort(404)

			else:
				actor.name = new_name				
				actor.age = new_age
				actor.gender = new_gender

			return jsonify({
				
			})

		except Exception as error:
			print(error)
			abort(422)

	@app.route('/movies/<int:id>', methods=['PATCH'])
	def update_movie(id):

		body = request.form
		new_title = body.get('title')
		new_release_date = body.get('release_date')

		try:
			movie = Movie.query.filter(Movie.id == id).one_or_more()

			if movie is None:
				abort(404)

			else:
				movie.title = new_title
				movie.release_date = new_release_date

			return jsonify({

			})
				
		except Exception as error:
			print(error)
			abort(422)

	return app
app = create_app()

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)