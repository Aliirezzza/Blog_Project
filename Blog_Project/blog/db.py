from flask import g
from pymongo import MongoClient
def get_db():
    if "db" not in g:
        client = MongoClient('mongodb://localhost:27017/')
        g.db = client["Blog"]

    return g.db