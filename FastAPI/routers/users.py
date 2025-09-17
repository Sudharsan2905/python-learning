from fastapi import APIRouter, HTTPException, status
from typing import List
from services.user import user_crud
from models.user import UserCreate
from schemas.user import UserResponse, UsersResponse

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=UsersResponse)
async def get_all_users():
    try:
        users = await user_crud.get_all_users()
        if not len(users):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No users found"
            )
        return UsersResponse(
            data=users,
            count=len(users),
            message="Users retrieved successfully"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving users: {str(e)}"
        )

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: str):
    user = await user_crud.get_user_by_id(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return UserResponse(data=user, message="User retrieved successfully")

@router.post("/create", response_model=UserResponse)
async def create_user(body: UserCreate):
    user_data = body.model_dump(exclude_unset=True)
    user = await user_crud.create_user(user_data)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User creation failed"
        )
    return UserResponse(data=user, message="User created successfully")