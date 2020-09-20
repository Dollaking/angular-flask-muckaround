import os
from flask import Flask, render_template, request
from flask_pymongo import PyMongo
import json


app = Flask(__name__)

# Mongo setup, connect to the db
app.config["MONGO_URI"] = "mongodb://localhost:27017/angular-flask-muckaround"
mongo = PyMongo(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/start', methods=['GET', 'POST'])
def send_data():
    errors = []
    results = {}
    try:
        data = json.loads(request.data.decode())
        first_name = data["first_name"]
        colour = data["colour"]
        mongo.db.people.insert_one({"name" : first_name,
                                    "colour": colour})
    except:
        print("Errors... :-(")
        errors.append("Couldn't get text")

    return render_template('index.html', errors=errors, results=results)

if __name__ == '__main__':
    app.run()
