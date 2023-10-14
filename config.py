
from pymongo import MongoClient

class Config:
    MONGODB_URI = "mongodb+srv://ratniq1:ratniq123@cluster0.rlggwd5.mongodb.net/ratniq?retryWrites=true&w=majority"

    @staticmethod
    def get_database():
        client = MongoClient(Config.MONGODB_URI )
        return client.jewelleryData
