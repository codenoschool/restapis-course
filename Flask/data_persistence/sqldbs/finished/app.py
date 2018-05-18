from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

from marshmallow import Schema, fields

import os


# This method to get an absolute path of a file works with all the operative systems.
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
"""
If you're using MySQL or PostegreSQL you'll need to use another connector.
Check the repository, video description or post where 
you found this code for more information about it.
"""
DB_URI = "sqlite:///" + os.path.join(BASE_DIR, "database.db")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Framework(db.Model):
    __tablename__ = "frameworks"

    # The id will be unique, cannot be null, and auto-increase.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

class FrameworkSchema(Schema):
    id = fields.Int()
    name = fields.Str()
        
# This route is irrelevant for the REST API, you can delete it if you want to.
@app.route("/")
def index():

    return "Hello World!"


# GET METHOD

@app.route("/api/frameworks/", methods=["GET"])
"""
For this endpoint we'll be using Marshmallow to serialize the framework
objects that we got from the query, and then serialize the result again
but this time through the jsonify function to give a proper JSON response.

You can use this method for the rest of the methods which won't be using
marshmallow by default.
"""
def get_frameworks():
    frameworks = Framework.query.all()
    frameworks_schema = FrameworkSchema(many=True)
    result, errors = frameworks_schema.dump(frameworks)

    return jsonify(result)

@app.route("/api/frameworks/<string:name>")
def get_framework_by_name(name):
    framework = Framework.query.filter_by(name=name).first()
    framework_dicc = dict(id=framework.id, name=framework.name)

    return jsonify(framework_dicc)


# POST METHOD

@app.route("/api/frameworks/", methods=["POST"])
def add_framework():
    new_framework = Framework(name=request.json["name"])
    db.session.add(new_framework)
    db.session.commit()

    framework_dicc = dict(id=new_framework.id, name=new_framework.name)

    return jsonify(framework_dicc)


# PUT METHOD

@app.route("/api/frameworks/<int:id>", methods=["PUT"])
def edit_framework(id):
    framework = Framework.query.get(id)
    framework.name = request.json["name"]

    db.session.commit()

    framework_dicc = dict(id=framework.id, name=framework.name)

    return jsonify(framework_dicc)


# DELETE METHOD

@app.route("/api/frameworks/<int:id>", methods=["DELETE"])
def delete_framework(id):
    framework = Framework.query.get(id)
    
    db.session.delete(framework)
    db.session.commit()

    return jsonify({"message": "ok"})

"""
Since Flask 1.0 we are invited to use the following method to execute the app:

GNU/Linux:
    export FLASK_APP=app.py

Windows OS:
    CMD:
        set FLASK_APP=app.py
    Powershell:
        $env:FLASK_APP = "app.py"

Additionally you can set FLASK_ENV=development for Debug Mode

You cand find more info about it here:
http://flask.pocoo.org/docs/1.0/quickstart/#a-minimal-application
"""
