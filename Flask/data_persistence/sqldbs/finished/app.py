from flask import Flask, request, jsonify

# Do not forget to install these libraries in your virtualenv
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_URI = "sqlite:///" + os.path.join(BASE_DIR, "database.db")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Framework(db.Model):
    __tablename__ = "frameworks"

    id = db.Column(db.Integer, primary_key=True)
    #name = db.Column(db.String(50), nullable=False, unique=True)
    name = db.Column(db.String(50))

class FrameworkSchema(Schema):
    id = fields.Int()
    name = fields.Str()

@app.route("/")
def index():

    return "Hello World!"

@app.route("/api/frameworks/")
def get_all_frameworks():
    frameworks = Framework.query.all()
    framework_schema = FrameworkSchema(many=True)
    results, errors = framework_schema.dump(frameworks)

    return jsonify(results)

@app.route("/api/frameworks/<string:name>", methods=["GET"])
def get_one_framework_by_name(name):
    framework = Framework.query.filter_by(name=name).first()
    framework_schema = FrameworkSchema()
    result, errors = framework_schema.dump(framework)

    return jsonify(result)

@app.route("/api/frameworks/", methods=["POST"])
def add_framework():
    new_framework = Framework(name=request.json["name"])
    db.session.add(new_framework)
    db.session.commit()

    framework_dict = {
            "id": new_framework.id,
            "name": new_framework.name
            }

    return jsonify(framework_dict)

@app.route("/api/frameworks/<int:id>", methods=["PUT"])
def edit_framework(id):
    framework = Framework.query.filter_by(id=id).first()
    framework.name = request.json["name"]

    db.session.commit()

    framework_dict = dict(id=framework.id, name=framework.name)

    return jsonify(framework_dict)

@app.route("/api/frameworks/<int:id>", methods=["DELETE"])
def delete_framework(id):
    framework = Framework.query.get(id)

    db.session.delete(framework)
    db.session.commit()

    return jsonify({"message": "ok"})
