from flask import Flask, jsonify, request
from flask_mongoalchemy import MongoAlchemy
from marshmallow import Schema, fields

app = Flask(__name__)
"""
There are several ways to create the database:
you can use the mongo shell to create the db manually,
you can use the Python Shell to create a document (which
will create the db),
you can push your first document through the POST method
of this Flask App

Don't forget to have MongoDB installed and available.
"""
app.config["MONGOALCHEMY_DATABASE"] = "restapiscourse"
"""
Check out the docs of flask_mongoalchemy for more info.
https://pythonhosted.org/Flask-MongoAlchemy/
"""
db = MongoAlchemy(app)

class Framework(db.Document):
    # You don't have to specify the ID row, it is created by default by mongo.
    # You can use the ID of the documents by "mongo_id" as a string.
    name = db.StringField()

class FrameworkSchema(Schema):
    # It takes the mongo_id attr and display it as "id".
    id = fields.Str(attribute="mongo_id")
    name = fields.Str()

@app.route("/")
def index():
    """
    This route is irrelevant for the REST API, you can delete it if you want to.
    """

    return "Hello World!"


# GET METHOD

@app.route("/api/frameworks/", methods=["GET"])
def get_frameworks():
    """
    This method uses the marshmallow library to serialize
    the frameworks objects and then serialize the result
    again to give a proper JSON response.

    You can use this method for the rest of the enpoints.
    """
    frameworks_schema = FrameworkSchema(many=True)
    frameworks = Framework.query.all()

    result, errors = frameworks_schema.dump(frameworks)

    return jsonify(result)

@app.route("/api/frameworks/<string:name>")
def get_framework_by_name(name):
    framework = Framework.query.filter(Framework.name == name).first()

    framework_dict = {
        # This method to format a string only works in Python >= 3.6
        "id": f"{framework.mongo_id}",
        "name": framework.name
    }

    return jsonify(framework_dict)


# POST METHOD

@app.route("/api/frameworks/", methods=["POST"])
def add_framework():
    new_framework = Framework(name=request.json["name"])
    new_framework.save()

    framework_dict = {
        "id": "{}".format(new_framework.mongo_id),
        "name": new_framework.name
    }

    return jsonify(framework_dict)


# PUT METHOD

@app.route("/api/frameworks/<string:id>", methods=["PUT"])
def edit_framework(id):
    framework = Framework.query.get(id)
    framework.name = request.json["name"]
    framework.save()

    framework_dict = {
        "id": "{}".format(framework.mongo_id),
        "name": framework.name
    }

    return jsonify(framework_dict)


# DELETE METHOD

@app.route("/api/frameworks/<string:id>", methods=["DELETE"])
def delete_framework(id):
    framework = Framework.query.get(id)
    framework.remove()

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
