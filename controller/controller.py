from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlmodel import select
from database import async_session
from models import User, Post
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

async def create_user(user: User):
    try:
        async with async_session() as session:
            new_user = User(name=user.name, username=user.username, password=user.password)
            session.add(new_user)
            await session.commit()
            await session.refresh(new_user)
            return new_user
    except SQLAlchemyError as e:
        logger.error("Bir hata meydana geldi: %s", str(e), exc_info=True)
        raise HTTPException(status_code=500, detail="User could not be created")

async def create_post(post: Post, user_id: int):
    try:
        async with async_session() as session:
            new_post = Post(post=post.post, like_count=post.like_count, comment=post.comment, user_id=user_id)
            session.add(new_post)
            await session.commit()
            await session.refresh(new_post)
            return new_post
    except SQLAlchemyError as e:
        logger.error("Bir hata meydana geldi: %s", str(e), exc_info=True)
        raise HTTPException(status_code=500, detail="Posts could not be created")

async def get_all_users():
    try:
        async with async_session() as session:
            result = await session.execute(select(User))
            users = result.scalars().all()  # Kullanıcıları almak için scalars() kullanıldı
            return users
    except SQLAlchemyError as e:
        logger.error("Bir hata meydana geldi: %s", str(e), exc_info=True)
        raise HTTPException(status_code=500, detail="All users could not be retrieved")

async def get_all_posts():
    try:
        async with async_session() as session:
            result = await session.execute(select(Post))
            posts = result.scalars().all()  # Postları almak için scalars() kullanıldı
            return posts
    except SQLAlchemyError as e:
        logger.error("Bir hata meydana geldi: %s", str(e), exc_info=True)
        raise HTTPException(status_code=500, detail="All posts could not be retrieved")

async def get_a_user(user_id: int):
    try:
        async with async_session() as session:
            sql_ = select(User).where(User.id == user_id)
            result = await session.execute(sql_)
            user = result.scalar_one_or_none()  # Kullanıcıyı almak için kullanıldı
            if user is None:
                raise HTTPException(status_code=404, detail="User not found")

            return user
    except SQLAlchemyError as e:
        logger.error("Bir hata meydana geldi: %s", str(e), exc_info=True)
        raise HTTPException(status_code=500, detail="User not found")

async def get_a_post(post_id: int):
    try:
        async with async_session() as session:
            sql_ = select(Post).where(Post.id == post_id)
            result = await session.execute(sql_)
            post = result.scalar_one_or_none()  # İlk postu almak için kullanılır

            if post is None:
                raise HTTPException(status_code=404, detail="Post not found")

            return post
    except SQLAlchemyError as e:
        logger.error("Bir hata meydana geldi: %s", str(e), exc_info=True)
        raise HTTPException(status_code=500, detail="Post not found")

async def update_post(post_id: int, post: Post):
    try:
        async with async_session() as session:
            sql_ = select(Post).where(Post.id == post_id)
            result = await session.execute(sql_)
            existing_post = result.scalar_one_or_none()  # Mevcut postu almak için kullanılır

            if existing_post is None:
                raise HTTPException(status_code=404, detail="Post not found")

            existing_post.post = post.post
            existing_post.like_count = post.like_count
            existing_post.comment = post.comment
            await session.commit()
            await session.refresh(existing_post)
            return existing_post
    except SQLAlchemyError as e:
        logger.error("Bir hata meydana geldi: %s", str(e), exc_info=True)
        raise HTTPException(status_code=500, detail="Post could not be updated")

async def update_user(user_id: int, user: User):
    try:
        async with async_session() as session:
            sql_ = select(User).where(User.id == user_id)
            result = await session.execute(sql_)
            existing_user = result.scalar_one_or_none()  # Mevcut kullanıcıyı almak için kullanılır

            if existing_user is None:
                raise HTTPException(status_code=404, detail="User not found")

            existing_user.name = user.name
            existing_user.username = user.username
            existing_user.password = user.password
            await session.commit()
            await session.refresh(existing_user)
            return existing_user
    except SQLAlchemyError as e:
        logger.error("Bir hata meydana geldi: %s", str(e), exc_info=True)
        raise HTTPException(status_code=500, detail="User could not be updated")

async def delete_post(post_id: int):
    try:
        async with async_session() as session:
            sql_ = select(Post).where(Post.id == post_id)
            result = await session.execute(sql_)
            existing_post = result.scalar_one_or_none()  # Mevcut postu almak için kullanılır

            if existing_post is None:
                raise HTTPException(status_code=404, detail="Post not found")

            await session.delete(existing_post)  # Mevcut postu sil
            await session.commit()
            return existing_post
    except SQLAlchemyError as e:
        logger.error("Bir hata meydana geldi: %s", str(e), exc_info=True)
        raise HTTPException(status_code=500, detail="Post could not be deleted")

async def delete_user(user_id: int):
    try:
        async with async_session() as session:
            sql_ = select(User).where(User.id == user_id)
            result = await session.execute(sql_)
            existing_user = result.scalar_one_or_none()  # Mevcut kullanıcıyı almak için kullanılır

            if existing_user is None:
                raise HTTPException(status_code=404, detail="User not found")

            await session.delete(existing_user)  # Mevcut kullanıcıyı sil
            await session.commit()
            return existing_user
    except SQLAlchemyError as e:
        logger.error("Bir hata meydana geldi: %s", str(e), exc_info=True)
        raise HTTPException(status_code=500, detail="User could not be deleted")







