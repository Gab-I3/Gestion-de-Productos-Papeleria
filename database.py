from pymongo import MongoClient
import certifi

MONGO_URI = 'mongodb+srv://gab:1234@cluster0.guyxuhc.mongodb.net/?appName=Cluster0'
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["dbb_products_app"]
    except ConnectionError:
        print('Error de conexión con la bdd')
    return db
