from pymongo import MongoClient

HOST = 'localhost'
PORT = 27017

def connect_db(db_name='mydb', coll_name='mapReduce'):
    client = MongoClient(host=HOST, port=PORT)
    db = client[db_name]
    coll = db[coll_name]
    return db, coll
