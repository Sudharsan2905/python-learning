from database.connection import get_db
from bson import ObjectId
from typing import List, Optional
from models.user import User
from datetime import datetime

class UserCRUD:
    def __init__(self):
        self.db = get_db()
        self.collection = self.db.users

    async def get_all_users(self) -> List[User]:
        try:
            db_users = self.collection.find({})
            users = []
            for user_doc in db_users:
                users.append(self._convert_to_user(user_doc))
            return users
        except Exception as e:
            print(f"Error retrieving users: {str(e)}")
            return []

    async def get_user_by_id(self, user_id: str) -> Optional[User]:
        try:
            user_doc = self.collection.find_one({"_id": ObjectId(user_id)})
            if user_doc:
                return self._convert_to_user(user_doc)
            return None
        except Exception as e:
            print(f"Invalid user ID format: {user_id}. Error: {str(e)}")
            return None

    async def create_user(self, user_data: dict) -> User:
        try:
            existing_user = self.collection.find_one({"email": user_data["email"]})
            if existing_user:
                raise Exception("User with this email already exists")
            user_data = {
                **user_data,
                "createdAt": datetime.utcnow(),
                "updatedAt": datetime.utcnow(),
                "is_active": True
            }
            result = self.collection.insert_one(user_data)
            user_doc = self.collection.find_one({"_id": result.inserted_id})
            return self._convert_to_user(user_doc)
        except Exception as e:
            print(f"Error creating user: {str(e)}")
            return None

    def _convert_to_user(self, user_doc: dict) -> User:
        """Convert MongoDB document to User model"""
        return User(
            id=str(user_doc["_id"]),
            username=user_doc["username"],
            email=user_doc["email"],
            created_at=user_doc.get("createdAt"),
            is_active=user_doc.get("is_active", True)
        )

# Create instance
user_crud = UserCRUD()