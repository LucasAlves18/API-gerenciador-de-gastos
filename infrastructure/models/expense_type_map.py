from infrastructure.database import Base
from sqlalchemy import Column, Integer, String


class ExpenseTypeMap(Base):
    __tablename__ = "expense_type"

    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
