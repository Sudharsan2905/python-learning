from pymongo import MongoClient
from pymongo.server_api import ServerApi
from typing import Optional
import os
from dotenv import load_dotenv

load_dotenv()

class MongoDB:
    client: Optional[MongoClient] = None

    @classmethod
    def get_database(cls):
        if cls.client is None:
            uri = os.getenv("MONGODB_URI")
            cls.client = MongoClient(uri, server_api=ServerApi('1'))
        return cls.client[os.getenv("DATABASE_NAME")]

# Global database instance
def get_db():
    return MongoDB.get_database()