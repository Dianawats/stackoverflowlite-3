
# StackOverflow-lite

#Challenge3:

StackOverflow-lite is a platform where people can ask questions and provide answers.

- This repository contains API endpoints for the above application intergrated with a database

## Technologies used

- `Python3.6` 
- `Flask` 
- `Virtualenv` 

## Running the tests
To run tests run this command below in your terminal

```
nosetests -v --with-coverage
```

## Installation
**Clone this _Repository_**
```
$ https://github.com/Dianawats/stackoverflowlite-3
```

**Install all the necessary _dependencies:**
```
$ pip3 install -r requirements.txt
```
**Running the app**
```
Run the server At the terminal or console type
$ Python run.py

```
## Versioning
```
This API is versioned using url versioning starting, with the letter 'v'
```
## End Points
|           End Point                      |            Functionality                   |
|   -------------------------------------- | -----------------------------------------  |
|     POST   api/v1/users/signup           |             Registers a new user           |
|     POST api/v1/question/user_id         |             Post User Questions            |
|     GET  api/v1/question/user_id/qtn_id  |             Get one user Question          |
|     GET  api/v1/question/user_id         |             Get one user Question          |
|     PUT api/v1/question/user_id/qtn_id   |             Edit user Question             |
|    DELETE api/v1/question/user_id/qtn_id |             Delete user Question           |



## Author
- [Dian](https://github.com/Dianawats)
