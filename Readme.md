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

## Login information

### Casting Assistant
```
Username: CastingA@capstone.com
Password: C123@casting
```

```
Access Token:
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImtSdjhnWWM0d01SNFJFX3dITnBLWCJ9.eyJpc3MiOiJodHRwczovL2Rldi01bnN2LW1mbS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEyYTUxOWE4ZmM0YmEwMDcxZjBiNWFjIiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2MzAyMDQwNDQsImV4cCI6MTYzMDI5MDQ0NCwiYXpwIjoiTW1hemtKRXFoYks5WGZhaUpHZkwxYk1ONlB1NG1vbmIiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.b7DLOVebReIU9Vv4ixUTKlqymG5GNzoQ857T7H9Jsvkg6HTZ8su26eHS2ZaYhUcXL_dWh1w8a6iFF0HKi6RvjMt_1Y8NVwSIs1JiSGPC9hbx7ofKeQ9DYB7U3uO17kPfOv-7VEumJTKb36VBFg5W5mcTEypvsSpK40oDGN1I-LSzUALcga8FKckSGOipvwvG1F1kz_jElP_CT3nwUGcOl7N3nFZea7yFBKrGVYE2Uzp59CL79_AeLVIkrV5OEvX6QC4KHZSf6fCbNjsdRM-bGdzar5gmVdt71CKfsMhBJACgqKhLai3xVrFDKo19ZoMDTz1Vk_APLJIwf-Rt4Diidg
```

### Casting Assistant
```
Username: CDirector@capstone.com
Password: D123@director
```

```
Access Token:
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImtSdjhnWWM0d01SNFJFX3dITnBLWCJ9.eyJpc3MiOiJodHRwczovL2Rldi01bnN2LW1mbS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEyYTZjZjZhYWFiMmYwMDZhZTA5NmZlIiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2MzAyMDQxMDQsImV4cCI6MTYzMDI5MDUwNCwiYXpwIjoiTW1hemtKRXFoYks5WGZhaUpHZkwxYk1ONlB1NG1vbmIiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvciIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3IiLCJwYXRjaDptb3ZpZSIsInBvc3Q6YWN0b3IiXX0.Pzr1WM9ePGkjfmP5HrB2IUva6Yewp1c7QBN0KoyDagrFJvy5qEgfUFv-4kDBuIBe_cyOtkFfR3SP28SyNGTYgk48QBSDwPl5TOrLaD-xjTMZNYzyzoQ5SK9ddxI_qdgT87Qgtm_kevlqfH8VbhLCZCg88zNyTXZxxLXGlQACpsr_MtfNDWfRfk6NeHjJ5pvM21M0D0aVA_7V9kRWjJKEfwWlGXS9toRKN3CnH4Vtxh4DVdmKo03i4T9oUHhrw1_NxLrVj47rqMFU0L8Mx-I3ZwC8cjXn_qfj2NqdhKz9irqkcOKAppunnwjLZHZXIlKkn4SVnw0uzWo00OUdI3uKfA
```

### Casting Assistant
```
Username: EProducer@capstone.com
Password: P123@Producer
```

```
Access Token:
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImtSdjhnWWM0d01SNFJFX3dITnBLWCJ9.eyJpc3MiOiJodHRwczovL2Rldi01bnN2LW1mbS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEyYTZlZjdhYWFiMmYwMDZhZTA5NzVhIiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2MzAyMDQxNTYsImV4cCI6MTYzMDI5MDU1NiwiYXpwIjoiTW1hemtKRXFoYks5WGZhaUpHZkwxYk1ONlB1NG1vbmIiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9yIiwicGF0Y2g6bW92aWUiLCJwb3N0OmFjdG9yIiwicG9zdDptb3ZpZSJdfQ.cnzMDPJTgA7lxLOc4ovofRA8bTJIubashBwtYMprwNiBZjwUws08XSodeh7ckfCOCx8SmNmTjFk7NxMhtNDUnZMF2jbYm1ylHFyVZjVgarMqFKVBLfPp3OuKAHNLb0daa0gcjHdJtCxL7-BieoJ3powG7KJe1dRiswbvnRYdLjIIFWZ1GdCiCiOHN8vA7QpGjmt6fI-3nERvJBS1zurdHuWD7L7CGcJwdlWo0Q9BImbPF44PKhhWAKzhN7P-aOrGOgD5QSp9fExR78G9YWUgWFHOAM3E378TnppDaZRxE8s9m7FcMY29CkSaXqUhtB2yZnkZL6pOyfjvADQmij4_fQ
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