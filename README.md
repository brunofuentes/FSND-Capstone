# Capstone - Final Project

Final project of Udacity full stack web developer nanodegree program.
This project objective is to build a REST API including an authentication & authorization in [Flask](https://flask.palletsprojects.com/en/2.0.x/), role-based control design patterns using [Auth0](https://www.auth0.com), hosted and in [Heroku](http://www.heroku.com/), .

Project URL: [https://fsnd-capstone-bvf.herokuapp.com/](https://fsnd-capstone-bvf.herokuapp.com/).

List of contents taught by the [Nanodegree course](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd0044) within its 5 modules/projects:

- Python 3
- Relational Database Architecture
- Modeling Data Objects with SQLAlchemy
- Internet protocols and communication
- Developing a Flask API
- Authentication and Access
- Authentication with Auth0
- Authentication in Flask
- Role-Based Access Control (RBAC)
- Testing Flask Applications
- Deploying applications using AWS and Heroku

## Key Dependencies

- [Python 3.6](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
- [Python-jose](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)

## API Reference - Casting Agency Specifications

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

### Roles:
- Casting Assistant
    - Can view actors and movies

- Casting Director
    - All permissions a Casting Assistant has and…
    - Add or delete an actor from the database
    - Modify actors or movies

- Executive Producer
    - All permissions a Casting Director has and…
    - Add or delete a movie from the database

### Models
Movies with attributes title and release date
Actors with attributes name, age and gender

### Endpoints
- GET /actors and /movies
- DELETE /actors/ and /movies/
- POST /actors and /movies and
- PATCH /actors/ and /movies/

### Tests
- One test for success behavior of each endpoint
- One test for error behavior of each endpoint
- At least two tests of RBAC for each role