# Casting Agency API

## Capstone Project for Udacity's Full Stack Developer NanoDegree Program

<br>

### Heroku Link : https://elmintrix-capstone.herokuapp.com <br>

### Local Link : http://localhost:5000 <br>

<br>

# Prerequistes

- ### Python 3.7.X
- ### PIP Depencies

```bash
pip install -r requirements.txt
```

# Running the server

### To run the server execute:

<br>

```bash
export DATABASE_URL=<database-connection-url>
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

# API Calls

### The application can run locally , The hosted Version is at <a>https://elmintrix-capstone.herokuapp.com</a>

<br>

### The application has three different types of roles:

<br>

- Casting Assistant

  - Can View Actors and movies
  - `get:actors, get:movies`

- Casting Director

  - All permissions a Casting Assistant has and
  - Add or delete an actor from the database
  - Modify actors or movies
  - `patch:actor, patch:movie, post:actor, post:movie`

- Executive Producer
  - All permissions a Casting Director has and
  - Add or delete a movie from the database
  - `delete:actor, delete:movie`

<br>

# Endpoints

## GET /actors

- General

  - gets the list of all the actors
  - requires `get:actors` permission

- Request Example :
  - `https://elmintrix-capstone.herokuapp.com/actors`

<summary>Sample Response</summary>

```json
{
  "actors": [
    {
      "id": 1,
      "name": "Mark Whalberg",
      "age": 49
    },
    {
      "id": 2,
      "name": "Tom Cruze",
      "age": 30
    }
  ],
  "success": true
}
```

### POST /actors

- General

  - creates a new actor
  - requires `post:actor` permission

- Request Body

  - name: string, required
  - age: integer, required

- Sample Request
  - `https://elmintrix-capstone.herokuapp.com/actors`
  - Request Body

```json
{
  "id": 1,
  "name": "Eddie",
  "age": "24"
}
```

<summary>Sample Response</summary>

```json
{
  "actor": {
    "id": 1,
    "name": "Eddie",
    "age": 24
  },
  "success": true
}
```

### PATCH /actors/{actor_id}

- General

  - updates the info for an actor
  - requires `patch:actor` permission

- Request Body (at least one of the following fields required)

  - name: string, optional
  - age: date, optional

- Sample Request
  - `https://elmintrix-capstone.herokuapp.com/actors/1`
  - Request Body

```json
{
  "name": "Keanu reeves"
}
```

<summary>Sample Response</summary>

```json
{
  "actor.id": 1,
  "success": true
}
```

### DELETE /actors/{actor_id}

- General

  - deletes the actor
  - requires `delete:actor` permission

- Sample Request
  - `https://elmintrix-capstone.herokuapp.com/actors/1`

<summary>Sample Response</summary>

```json
{
  "actor_id": {
    "age": 18,
    "id": 1,
    "name": "MeoMeo"
  },
  "success": true
}
```

### GET /movies

- General

  - gets the list of all the movies
  - requires `get:movies` permission

- Sample Request
  - `https://elmintrix-capstone.herokuapp.com/movies`

<summary>Sample Response</summary>

```json
{
  "movies": [
    {
      "id": 1,
      "release_date": "Mon, 12 Dec 2022 00:00:00 GMT",
      "title": "The Matrix 4"
    },
    {
      "id": 2,
      "release_date": "Mon, 23 Apr 2012 00:00:00 GMT",
      "title": "Interstellar 2"
    }
  ],
  "success": true
}
```

### POST /movies

- General

  - creates a new movie
  - requires `post:movie` permission

- Request Body

  - title: string, required
  - release_date: Date, required

- Sample Request
  - `https:/elmintrix-capstone.herokuapp.com/actors`
  - Request Body

```json
{
  "title": "The Matrix 4",
  "release_date": "2012-04-23"
}
```

<summary>Sample Response</summary>

```json
{
  "movie": {
    "id": 1,
    "release_date": "Mon, 23 Apr 2012 00:00:00 GMT",
    "title": "The Matrix 4"
  },
  "success": true
}
```

#### PATCH /movie/{movie_id}

- General

  - updates the info for a movie
  - requires `patch:movie` permission

- Request Body (at least one of the following fields required)

  - title: string, optional
  - release_date: Date, optional

- Sample Request
  - `https://elmintrix-capstone.herokuapp.com/movies/3`
  - Request Body

```json
{
  "title": "HitMan 3"
}
```

<summary>Sample Response</summary>

```json
{
  "actor.id": 2,
  "success": true
}
```

#### DELETE /movies/{movie_id}

- General

  - deletes the movie
  - requires `delete:movie` permission
  - will not affect the actors present in the database

- Sample Request
  - `https://elmintrix-capstone.herokuapp.com/movies/3`

<summary>Sample Response</summary>

```json
{
  "movie": {
    "id": 3,
    "release_date": "Mon, 23 Apr 2012 00:00:00 GMT",
    "title": "The Matrix 4"
  },
  "success": true
}
```
