from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/frameworks/")
def get_frameworks():

    return jsonify(result)

@app.route("/api/frameworks/<string:name>")
def get_framework_by_name(name):

    return jsonify(data)

@app.route("/api/frameworks/", methods=["POST"])
def add_framework():

    return jsonify(new_framework)

@app.route("/api/frameworks/<string:id>", methods=["PUT"])
def edit_framework(id):

    return jsonify(data)

@app.route("/api/frameworks/<string:id>", methods=["DELETE"])
def delete_framework(id):

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
