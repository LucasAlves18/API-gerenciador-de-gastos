from infraestrutura.database import Base
from sqlalchemy import Column, Integer, String


class TipoDespesas(Base):
    __tablename__ = "tipo_despesas"

    id = Column(Integer, primary_key=True)
    descricao = Column(String, nullable=False)
