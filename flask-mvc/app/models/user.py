from flask_pymongo import PyMongo
from pymongo import MongoClient

class UserModel:
    def __init__(self, mongo):
        self.mongo = mongo
        self.collection = self.mongo.users

    def create_user(self, data):
        return self.collection.insert_one(data)

    def get_all_users(self):
        return self.collection.find()
