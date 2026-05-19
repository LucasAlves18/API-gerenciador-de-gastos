from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
from infraestrutura.models import user_map
from infraestrutura.models import despesas_map
from infraestrutura.models import tipo_despesas
from infraestrutura.models import  tipo_pagamento_map
engine = create_engine("sqlite:///banco.db")
engine.connect()
Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()