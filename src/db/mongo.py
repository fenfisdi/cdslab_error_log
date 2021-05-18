from os import environ

from mongoengine import connect

from src.utils import Singleton


class MongoEngine(metaclass=Singleton):
    def __init__(self):
        self.mongo_uri = environ.get('MONGO_URI')

    def get_connection(self):
        return connect(host=self.mongo_uri)
