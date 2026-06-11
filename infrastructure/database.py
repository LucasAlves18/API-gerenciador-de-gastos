from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
from infrastructure.models import user_map
from infrastructure.models import expense_map
from infrastructure.models import expense_type_map
from infrastructure.models import  payment_type_map
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