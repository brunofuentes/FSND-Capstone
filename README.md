# Capstone - Final Project

Final project of Udacity full stack web developer nanodegree program.
This project objective is to build a REST API including an authentication & authorization in [Flask](https://flask.palletsprojects.com/en/2.0.x/), role-based control design patterns using [Auth0](https://www.auth0.com), hosted and in [Heroku](http://www.heroku.com/).

API URL: [https://fsnd-capstone-bvf.herokuapp.com/](https://fsnd-capstone-bvf.herokuapp.com/).

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

## Tech Stack (Dependencies)

- **virtualenv** as a tool to create isolated Python environments
- [Python 3.6](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
- [Python-jose](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)

## Running the App localy

1. Clone this Repository
2. Initialize and activate a virtualenv: 
```
pip install virtualenv
python -m virtualenv env
```

3. Install all dependencies: 
```
pip install requirements.txt
``` 

5. Start server by running:
```
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

## API Reference - Casting Agency Specifications

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

## Roles:

To generate a new token:

```
https://fsnd-learning.eu.auth0.com/authorize?
audience=castingagency&
response_type=token&
client_id=k45gdNHT8UN58n5grMnUnOnd4WBJZLEL&
redirect_uri=https://fsnd-capstone-bvf.herokuapp.com/
```

- Casting Assistant
    - Can view actors and movies

Login info:
- email: assistant@FSND-Casting.com
- password: Assistant123

- Casting Director
    - All permissions a Casting Assistant has and…
    - Add or delete an actor from the database
    - Modify actors or movies

Login info:
- email: director@FSND-Casting.com
- password: Director123

- Executive Producer
    - All permissions a Casting Director has and…
    - Add or delete a movie from the database

Login info:
- email: producer@FSND-Casting.com
- password: Producer123

## Models:
- Movies with attributes title and release date
- Actors with attributes name, age and gender

## Endpoints:


### GET '/'

- Returns a simple message to confirm server is running.

Sample:

```
{
"message": "Healthy!",
"success": true
}
```

### GET '/actors'

- Returns a list of all actors from the database

Sample:

```
{
    "actors": [
        {
            "age": 68,
            "gender": "Fem",
            "id": 1,
            "name": "Fernanda Montenegro"
        }
    ],
    "success": true
}
```

### GET '/movies'

- Returns a list of all movies from the database. Requires access authorization (Casting assistant, Casting director or Executive Producer)

Sample:

```
{
    "movies": [
        {
            "id": 1,
            "release_date": "1994",
            "title": "Pulp Fiction"
        }
    ],
    "success": true
}
```

### DELETE '/actors/<int:actor_id>'

- Deletes a specific actor from the database. Requires specific access (Casting director or Executive Producer)
- Returns the deleted actor information (id, name, age, gender)

Sample:

```
{
    "deleted": {
        "age": 78,
        "gender": "Masc",
        "id": 2,
        "name": "Morgan Freeman"
    },
    "success": true
}
```

### DELETE '/movies/<int:movie_id>'

- Deletes a specific movie from the database. Requires specific access (Executive Producer only)
- Returns the deleted movie information (id, title, release date)

Sample:

```
{
    "deleted": {
        "id": 2,
        "release_date": "1997",
        "title": "Titanic"
    },
    "success": true
}
```

### POST '/actors'

- Create a new actor. Requires specific access (Casting director or Executive Producer)
- Returns the created actor information (id, name, age, gender)

Sample:

```
{
    "created actor": {
        "age": 78,
        "gender": "Masc",
        "id": 2,
        "name": "Morgan Freeman"
    },
    "success": true
}
```

### POST '/movies'

- Creates a new movie. Requires specific access (Executive Producer only)
- Returns the created movie information (id, title, release date)

Sample:

```
{
    "created movie": {
        "id": 2,
        "release_date": "1997",
        "title": "Titanic"
    },
    "success": true
}
```

### PATCH '/actors/<int:actor_id>'

- Updates the values from a specific actor register. Requires specific access (Casting director or Executive Producer)
- Returns the modified actor information (id, name, age, gender)

Sample:

```
{
    "actor": {
        "age": 69,
        "gender": "Fem",
        "id": 1,
        "name": "Fernanda Montenegro"
    },
    "success": true
}
```

### PATCH '/movies/<int:movie_id>'

- Updates the values from a specific movie register. Requires specific access (Casting director or Executive Producer)
- Returns the modified actor information (id, title, release date)

Sample:

```
{
    "movie": {
        "id": 1,
        "release_date": "1995",
        "title": "Pulp Fiction"
    },
    "success": true
}
```

### Tests:

- One test for success behavior of each endpoint
- One test for error behavior of each endpoint
- At least two tests of RBAC for each role

How to run the tests:

```
python test_app.py
```