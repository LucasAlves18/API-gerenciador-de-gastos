from infraestrutura.database import Base
from sqlalchemy import Column, Integer, String


class TipoPagamento(Base):
    __tablename__ = "tipo_pagamento"

    id = Column(Integer, primary_key=True)
    descricao = Column(String, nullable=False)
