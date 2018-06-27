from flask import Flask, jsonify, request
from flask_mongoalchemy import MongoAlchemy
from marshmallow import Schema, fields

app = Flask(__name__)
app.config["MONGOALCHEMY_DATABASE"] = "restapiscourse"
db = MongoAlchemy(app)

class Framework(db.Document):
    name = db.StringField()

class FrameworkSchema(Schema):
    id = fields.Str(attribute="mongo_id")
    name = fields.Str()

@app.route("/")
def index():

    return "Hello World!"


# GET METHOD

@app.route("/api/frameworks/", methods=["GET"])
def get_frameworks():
    frameworks = Framework.query.all()
    framework_schema = FrameworkSchema(many=True)
    results, errors = framework_schema.dump(frameworks)

    return jsonify(results)

@app.route("/api/frameworks/<string:name>")
def get_framework_by_name(name):
    framework = Framework.query.filter(Framework.name == name).first()
    framework_schema = FrameworkSchema()
    result = framework_schema.dump(framework)

    return jsonify(result)


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
        # This method to format a string only works in Python >= 3.6
        "id": f"{framework.mongo_id}",
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
