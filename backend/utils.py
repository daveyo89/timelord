import os

from pymongo import MongoClient


def get_db_handle():
    client = MongoClient(os.getenv('MONGODB_URI'))
    db = client.test

    return db, client
