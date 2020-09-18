# JAJAC Test CRUD App

## Resources

https://realpython.com/flask-by-example-integrating-flask-and-angularjs/

## Requirements

- python3
- python3-venv
- python3-flask
- mongodb

## Setting up a virtual Environment

A virtual environment allows us to keep all our required packages within our project. We then add the packages to our `.gitignore`. This stops our project from vommitting all over our system and leaving redundant packages once the project is finished. If you don't care, just run `pip3 install -r requirements.txt`

#### Creating the virtual environment

From root directory:

Create the python virtual environment directory (ignored in `.gitignore`):

`python3 -m venv env`


#### Setting your virtual environment in your current terminal

Source that virtual environment before each run

`source env/bin/activate`

#### Leaving the virtual environment

Leaving the virtual:

`deactivate`

#### Adding packages to the project

After sourcing the environment:

`pip3 install foo`

or for specific version

`pip3 install foo==3.1.2`

Saving this package to the list of requirements:

`pip3 freeze > requirements.txt`


## Running the project

#### Locally 

`source env/bin/activate`

`python manage.py runserver`

#### Server

`source env/bin/activate`

`python3 manage.py runserver --host=0.0.0.0`
