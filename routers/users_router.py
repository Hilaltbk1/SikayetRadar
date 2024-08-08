from fastapi import APIRouter
from controller.controller import get_all_users, get_a_user, create_user, update_user, delete_user
from models import User


router = APIRouter(
    prefix="/users",
    tags=['Users']
)


@router.get('/allusers/')
async def all_users():
    return get_all_users()


@router.get('/users/{user_id}')
async def get_user_by_id(user_id: int):
    return get_a_user(user_id)


@router.post('/users/', response_model=User)
async def create_user_endpoint(user: User):
    return create_user(user)


@router.put("/update_user/{user_id}", response_model=User)
async def update_user_endpoint(user_id: int, user: User):
    return update_user(user_id, user)


@router.delete('/delete_user/{user_id}')
async def delete_user_endpoint(user_id: int):
    return delete_user(user_id)
