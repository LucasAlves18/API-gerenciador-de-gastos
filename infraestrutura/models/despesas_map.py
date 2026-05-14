from infraestrutura.database import Base
from sqlalchemy import Column, Integer, String, Float


class DespesasMap(Base):
    __tablename__ = "despesas"

    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, nullable=False)
    id_tipo_pagamento = Column(Integer, nullable=False) # futuro fk
    valor = Column(Float, nullable=False)
    descricao = Column(String)
