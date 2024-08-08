from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "mysql://root:hellohilal123@127.0.0.1:3306/mydatabase1"

engine = create_engine(DATABASE_URL, echo=True)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
