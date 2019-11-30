from . import Goal
from app import mongo
from umongo import Document, fields

@mongo.register
class User(Document):
    email = fields.EmailField(primary_key=True, required=True)
    username = fields.StrField(required=True)
    # goals = fields.EmbeddedDocumentListField(Goal.Goal)