from pymongo import MongoClient


def connect():

    client = MongoClient("localhost")
    db = client["Escolar"]
    collections = db["profesores"]
    return collections
