from pymongo import MongoClient

def get_mongodb():
    client = MongoClient('mongodb+srv://qwerrewq:qwerrewq@mycluster.a3vheay.mongodb.net/?retryWrites=true&w=majority')

    db = client.myDatabase9
    return db