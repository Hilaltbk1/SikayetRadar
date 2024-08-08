from fastapi import APIRouter
from controller.controller import get_all_posts, get_a_post, create_post, update_post, delete_post
from models import Post


router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)


@router.get('/allposts/')
async def all_posts():
    return get_all_posts()


@router.get('/posts/{post_id}')
async def get_post_by_id(post_id: int):
    return get_a_post(post_id)


@router.post('/posts/', response_model=Post)
async def create_post_endpoint(post: Post):
    return create_post(post)


@router.put("/update_post/{post_id}", response_model=Post)
async def update_post_endpoint(post_id: int, post: Post):
    return update_post(post_id, post)


@router.delete('/delete_post/{post_id}')
async def delete_post_endpoint(post_id: int):
    return delete_post(post_id)
