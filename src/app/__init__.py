
import os
from flask import Flask
# from flask_pymongo import PyMongo
import json                       
import datetime                       
from bson.objectid import ObjectId
from pymongo import MongoClient
from umongo import Instance

app = Flask(__name__)

# add mongo url to flask config, so that flask_pymongo can use it to make connection
# app.config['MONGO_URI'] = os.environ.get('DB')
# mongo = PyMongo(app)


dbClient = MongoClient(host=os.environ.get('MONGO_HOST'), port=int(os.environ.get('MONGO_PORT')))
mongo = Instance(dbClient.db)

class JSONEncoder(json.JSONEncoder):                           
    ''' extend json-encoder class'''
    def default(self, o):
        return o.__dict__                 
        # if isinstance(o, ObjectId):
        #     return str(o)                               
        # if isinstance(o, datetime.datetime):
        #     return str(o)
        # return json.JSONEncoder.default(self, o)