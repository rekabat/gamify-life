from app import app, JSONEncoder
from model.User import User
from flask import request, jsonify
from bson.objectid import ObjectId

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/users", methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        users = User.find({})
        userdump = []
        for u in users:
            userdump.append(u.dump())
        return jsonify(userdump)
    else:
        User(
            email="fake@fake.com",
            username="Person McFakerson").commit()
        return 'yes'

@app.route("/users/<id>", methods=['GET'])
def user(id):
    user = User.find_one({'_id': ObjectId(id)})
    return user.dump()