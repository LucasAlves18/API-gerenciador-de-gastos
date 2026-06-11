from infrastructure.database import Base
from sqlalchemy import Column, Integer, String, Float


class UserMap(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    balance = Column(Float, default=0.0)
