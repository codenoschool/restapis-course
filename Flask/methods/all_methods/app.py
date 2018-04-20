from flask import Flask, jsonify, request

app = Flask(__name__)

frameworks = [
        {
            "id": 1,
            "name": "Flask"
            },
        {
            "id": 2,
            "name": "ExpressJS"
            },
        {
            "id": 3,
            "name": "Laravel"
            }
        ]

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
    framework = []
    for f in frameworks:
        if f["name"] == name:
            framework.append(f)

    return jsonify(framework[0])


# POST METHOD

@app.route("/api/frameworks/", methods=["POST"])
def add_framework():
    #framework = request.json
    framework = {
            "id": request.json["id"],
            "name": request.json["name"]
            }
    frameworks.append(framework)

    return jsonify(framework)


# PUT METHOD

@app.route("/api/frameworks/<int:id>", methods=["PUT"])
def edit_framework(id):
    framework = [framework for framework in frameworks if framework["id"] == id]

    framework = framework[0]
    framework["id"] = request.json["id"]
    framework["name"] = request.json["name"]

    return jsonify(framework)


# DELETE METHOD

@app.route("/api/frameworks/<int:id>", methods=["DELETE"])
def delete_framework(id):
    framework = [framework for framework in frameworks if framework["id"] == id]

    frameworks.remove(framework[0])

    return jsonify({"message": "ok"})

if __name__ == "__main__":
    # Debug mode is only for development mode.
    app.run(debug=True)
