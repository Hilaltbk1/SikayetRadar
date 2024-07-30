from fastapi import FastAPI
from controller.controller import (get_all_users, get_a_user, get_a_post, get_all_posts, update_user, update_post,
                                   create_user, create_post, delete_user, delete_post)
from models import User, Post
from database import init_db

app = FastAPI()


@app.on_event("startup")
def on_startup():
    init_db()


@app.get('/allusers/')
async def all_users():
    return get_all_users()


@app.get('/allposts/')
async def all_posts():
    return get_all_posts()


@app.get('/users/{user_id}')
async def get_user_by_id(user_id: int):
    return get_a_user(user_id)


@app.get('/posts/{post_id}')
async def get_post_by_id(post_id: int):
    return get_a_post(post_id)


@app.post('/users/', response_model=User)
async def create_user_endpoint(user: User):
    return create_user(user)


@app.post('/posts/', response_model=Post)
async def create_post_endpoint(post: Post):
    return create_post(post)


@app.put("/update_post/{post_id}", response_model=Post)
async def update_post_endpoint(post_id: int, post: Post):
    return update_post(post_id, post)


@app.put("/update_user/{user_id}", response_model=User)
async def update_user_endpoint(user_id: int, user: User):
    return update_user(user_id, user)


@app.delete('/delete_post/{post_id}')
async def delete_post_endpoint(post_id: int):
    return delete_post(post_id)


@app.delete('/delete_user/{user_id}')
async def delete_user_endpoint(user_id: int):
    return delete_user(user_id)
