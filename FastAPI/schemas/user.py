from pydantic import BaseModel
from typing import List
from models.user import User

class UserResponse(BaseModel):
    success: bool = True
    data: User
    message: str = ""

class UsersResponse(BaseModel):
    success: bool = True
    data: List[User]
    count: int
    message: str = ""