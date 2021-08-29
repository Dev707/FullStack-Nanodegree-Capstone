
# FullStack Nanodegree Capstone

I'd like to thank the Misk Foundation and Udacity for this wonderful opportunity
A special thanks to MJ, who recommended that I enrolled in this wonderful program (:

## Overview
Casting Agency is FSND Capstone Project for Udacity

Heroku Link @ [https://ksg-capstone.herokuapp.com/](https://ksg-capstone.herokuapp.com/)

Local Link @ [http://localhost:5000](http://localhost:5000) <br>
  
## Home page
![SCREENSHOT](examples/homepage.png)

## Login Page
![SCREENSHOT](examples/login.png)

## Project Dependencies

- ### Python 3.7.X

- ### PIP Depencies

```bash
pip install -r requirements.txt
```
  

## API Calls

The application can run locally , The hosted Version is @ <a>https://ksg-capstone.herokuapp.com/</a>

### To run the server execute:

<br>

```bash
export DATABASE_URL=<DB-connection-url>
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

<br>

### Roles permissions:

<br>

- Casting Assistant

  - `get:actors, get:movies`

- Casting Director

  - `patch:actor, patch:movie, post:actor, post:movie`

- Executive Producer

  - `delete:actor, delete:movie`

<br>


### Error Handling

The API will return the following error codes when requests fail:

- 400: Bad Request

- 401: unauthorized

- 401: Authorization header must start with "Bearer"

- 401: Token not found

- 401: Authorization header must be bearer token

- 401: Authorization malformed

- 401: Token expired

- 403: permission not found

- 404: Resource Not Found

- 422: Not Processable

- 500: Internal Server Error

  

An example of 401 error due to RBAC returned as JSON objects in the following format:

```

{

"error": 401,

"message": {

"code": "authorization_header_missing",

"description": "Authorization header is expected."

},

"success": false

}

```

  

Other errors are returned as JSON objects in the following format:

```

{

"success": False,

"error": 400,

"message": "bad request"

}

```


### API Endpoints


#### GET '/actors'


```
{
    "actors": [
        {
            "age": 15,
            "id": 1,
            "name": "Abdullah MK"
        },
        {
            "age": 15,
            "id": 2,
            "name": "Steve Jobs"
        }
    ],
    "success": true
}
  

```

#### POST '/actors'

```
Body:
{
    "name":"Mjeed Jerry",
    "age":20
}

Response:
{
    "actor": {
        "age": 20,
        "id": 3,
        "name": "Mjeed Jerry"
    },
    "success": true
}
```

#### PATCH '/actors/1'

```
Body:
{
    "name":"Mr Apple" 
}

Response:
{
    "actor.id": 1,
    "success": true
}
```

#### DELETE '/actors/1'

```
{
    "delete": 1,
    "success": true
}
```

#### GET '/movies'

```
{
    "movies": [
        {
            "id": 1,
            "release_date": "Tue, 23 Apr 2019 00:00:00 GMT",
            "title": "The Matrix 2"
        },
        {
            "id": 2,
            "release_date": "Fri, 12 Jun 2020 00:00:00 GMT",
            "title": "Free guy"
        },
        {
            "id": 3,
            "release_date": "Wed, 11 Aug 2021 00:00:00 GMT",
            "title": "reminiscence"
        }
    ],
    "success": true
}
```

#### POST '/movies'

```
Body:
{
    "title":"reminiscence",
    "release_date":"2021-08-11"
}

Response:
{
    "movie": {
        "id": 3,
        "release_date": "Wed, 11 Aug 2021 00:00:00 GMT",
        "title": "reminiscence"
    },
    "success": true
}
```

#### PATCH '/movies/1'

```
Body:
{
    "title":"Iphone movie" 
}

Response:
{
    "movie": 1,
    "success": true
}
```

#### DELETE '/movies/1'

```
{
    "delete": 1,
    "success": true
}
```

## Testing

* From within the project directory first ensure you are working using your created virtual environment.

* Run the setup file to create the environment variables.
  
```bash
source setup.sh
```

Run the unittest using below command

```
python test_app.py
```

### Result
```
........
----------------------------------------------------------------------
Ran 8 tests in 30.287s

OK
```

### Testing with Postman collection
You have to update token if it expierd, [Postman collection](capstone.postman_collection.json)