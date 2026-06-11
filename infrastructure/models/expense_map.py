from infrastructure.database import Base
from sqlalchemy import Column, Integer, String, Float


class ExpenseMap(Base):
    __tablename__ = "expense"

    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, nullable=False)
    id_payment_type = Column(Integer, nullable=False) # futuro fk
    value = Column(Float, nullable=False)
    description = Column(String)
