from fastapi import HTTPException
from sqlmodel import select, Session
from database import engine
from models import User, Post


def create_user(user: User):
    """
    Creates a new user in the database.

    :param user: An instance of the User model containing the user's details.
    :return: The newly created user with updated information.
    """
    with Session(engine) as session:
        new_user = User(name=user.name, username=user.username, password=user.password)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return new_user


def create_post(post: Post):
    """
    Creates a new post in the database.

    :param post: An instance of the Post model containing the post's details.
    :return: The newly created post with updated information.
    """
    with Session(engine) as session:
        new_post = Post(post=post.post, like_count=post.like_count, comment=post.comment)
        session.add(new_post)
        session.commit()
        session.refresh(new_post)
        return new_post


def get_all_users() :
    """
    Retrieves a list of all users in the database.

    :return: A list of all users in the database.
    """
    with Session(engine) as session:
        users = session.exec(select(User)).all()
        return users


def get_all_posts() :
    """
    Retrieves a list of all posts in the database.

    :return: A list of all posts in the database.
    """
    with Session(engine) as session:
        posts = session.exec(select(Post)).all()
        return posts


def get_a_user(user_id: int):
    """
    Retrieves a specific user from the database.

    :param user_id: The ID of the user to retrieve.
    :return: A specific user from the database.
    """
    with Session(engine) as session:
        sql_ = select(User).where(User.id == user_id)
        result = session.exec(sql_).first()

        if result is None:
            raise HTTPException(status_code=404, detail="User not found")

        return result


def get_a_post(post_id: int):
    """
    Retrieves a specific post from the database.

    :param post_id: The ID of the post to retrieve.
    :return: A specific post from the database.
    """
    with Session(engine) as session:
        sql_ = select(Post).where(Post.id == post_id)
        result = session.exec(sql_).first()

        if result is None:
            raise HTTPException(status_code=404, detail="Post not found")

        return result


def update_post(post_id: int, post: Post):
    """
    Updates a specific post in the database.

    :param post_id: The ID of the post to update.
    :param post: An instance of the Post model containing the post's details.
    :return: The updated post from the database.
    """
    with Session(engine) as session:
        sql_ = select(Post).where(Post.id == post_id)
        result = session.exec(sql_).first()

        if result is None:
            raise HTTPException(status_code=404, detail="Post not found")

        result.post = post.post
        result.like_count = post.like_count
        result.comment = post.comment
        session.commit()
        session.refresh(result)
        return result


def update_user(user_id: int, user: User):
    """
    Updates a specific user in the database.

    :param user_id: The ID of the user to update.
    :param user: An instance of the User model containing the user's details.
    :return: The updated user from the database.
    """
    with Session(engine) as session:
        sql_ = select(User).where(User.id == user_id)
        result = session.exec(sql_).first()

        if result is None:
            raise HTTPException(status_code=404, detail="User not found")

        result.name = user.name
        result.username = user.username
        result.password = user.password
        session.commit()
        session.refresh(result)
        return result


def delete_post(post_id: int):
    """
    Deletes a specific post from the database.

    :param post_id: The ID of the post to delete.
    :return: The deleted post from the database.
    """
    with Session(engine) as session:
        sql_ = select(Post).where(Post.id == post_id)
        result = session.exec(sql_).one_or_none()

        if result is None:
            raise HTTPException(status_code=404, detail="Post not found")

        session.delete(result)
        session.commit()
        return result


def delete_user(user_id: int):
    """
    Deletes a specific user from the database.

    :param user_id: The ID of the user to delete.
    :return: The deleted user from the database.
    """
    with Session(engine) as session:
        sql_ = select(User).where(User.id == user_id)
        result = session.exec(sql_).one_or_none()

        if result is None:
            raise HTTPException(status_code=404, detail="User not found")

        session.delete(result)
        session.commit()
        return result
