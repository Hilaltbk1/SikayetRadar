from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship, create_engine, MetaData

# MetaData nesnesini oluşturun
metadata = MetaData()

class User(SQLModel, table=True, metadata=metadata):
    __tablename__ = "user"  # Tablo adını açıkça belirtin
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    username: str
    password: str
    posts: List["Post"] = Relationship(back_populates="user")

    # extend_existing parametresini kullanın
    __table_args__ = {'extend_existing': True}
