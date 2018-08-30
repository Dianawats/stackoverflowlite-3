# StackOverflow-lite
#Challenge3:

StackOverflow-lite is a platform where people can ask questions and provide answers.

- This repository contains API endpoints for the above application intergrated with a database

## Technologies used

- `Python3.6` - Programming language that lets you work more quickly
- `Flask` - Python based web framework
- `Virtualenv` - A tool to create isolated virtual environment

## Running the tests
To run tests run this command below in your terminal

```
nosetests -v --with-coverage
```

## Installation
**Clone this _Repository_**
```
$ https://github.com/Dianawats/StackOverflow-lite.git
$ cd StackOverflow-lite
```
**Create virtual environment and install it**
```
$ virtualenv --python=python3 venv
$ source /venv/bin/activate
```
**Install all the necessary _dependencies_ by**
```
$ pip3 install -r requirements.txt
```
**Run _app_ by**

```
Run the server At the terminal or console type
$ Python run.py
```
## Versioning
```
This API is versioned using url versioning starting, with the letter 'v'
This is version one"v1" of the API
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

## Contributors
- [Dian](https://github.com/Dianawats)
