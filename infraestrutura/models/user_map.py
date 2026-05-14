from infraestrutura.database import Base
from sqlalchemy import Column, Integer, String, Float


class UserMap(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    senha = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    saldo = Column(Float, default=0.0)
