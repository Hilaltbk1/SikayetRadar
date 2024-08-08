from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from models import User


class Post(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    post: str
    like_count: int = Field(default=0)
    comment: str = Field(default="")
    user_id: int = Field(default=None, foreign_key="user.id")
    user: Optional["User"] = Relationship(back_populates="posts")

