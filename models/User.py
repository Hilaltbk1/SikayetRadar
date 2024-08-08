from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship
from models import Post


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    username: str
    password: str
    posts: List["Post"] = Relationship(back_populates="user")







