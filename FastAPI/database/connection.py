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
        try:
            if cls.client is None:
                uri = os.getenv("MONGODB_URI")
                cls.client = MongoClient(uri, server_api=ServerApi('1'))
                print("Database Connection successfully")
            return cls.client[os.getenv("DATABASE_NAME")]
        except Exception as e:
            print("Database Connection Failed", e)

# Global database instance
def get_db():
    return MongoDB.get_database()