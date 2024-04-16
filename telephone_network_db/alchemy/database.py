from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, DeclarativeBase


engine = create_engine(
    url="sqlite:///C:/Users/Никита/PycharmProjects/telephone_network_4var/telephone_network_db/telephone_network_db.sqlite",
    echo=False,
    pool_size=5,
    max_overflow=10,
)

session_factory = sessionmaker(engine)


class Base(DeclarativeBase):
    pass





