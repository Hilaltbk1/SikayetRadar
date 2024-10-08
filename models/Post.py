from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship, create_engine, MetaData

from models import User


class Post(SQLModel, table=True):
    __tablename__ = "post"
    __table_args__ = {'extend_existing': True}  # Mevcut tabloyu güncelleyebilirsiniz

    id: Optional[int] = Field(default=None, primary_key=True)
    post: str
    like_count: int = Field(default=0)
    comment: str = Field(default="")
    user_id: int = Field(foreign_key="user.id")
    user: Optional[User] = Relationship(back_populates="posts")
