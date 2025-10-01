from sqlalchemy import create_engine
from sqlalchemy.orm import Session

# from settings import Settings
from settings import DATABASE_URL

# engine = create_engine(Settings().DATABASE_URL)
engine = create_engine(DATABASE_URL)  # pyright: ignore[reportArgumentType]


def get_session():
    with Session(engine) as session:
        yield session
