from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

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
        
# This route is irrelevant for the REST API, you can delete it if you want to.
@app.route("/")
def index():

    return "Hello World!"


# GET METHOD

@app.route("/api/frameworks/", methods=["GET"])
def get_frameworks():

    return jsonify(frameworks)

@app.route("/api/frameworks/<string:name>")
def get_framework_by_name(name):

    return jsonify(framework)


# POST METHOD

@app.route("/api/frameworks/", methods=["POST"])
def add_framework():

    return jsonify(framework)


# PUT METHOD

@app.route("/api/frameworks/<int:id>", methods=["PUT"])
def edit_framework(id):

    return jsonify(framework)


# DELETE METHOD

@app.route("/api/frameworks/<int:id>", methods=["DELETE"])
def delete_framework(id):

    return jsonify({"message": "ok"})

if __name__ == "__main__":
    # This is only for development.
    db.create_all()
    app.run(debug=True)
