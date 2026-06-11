from infrastructure.database import Base
from sqlalchemy import Column, Integer, String


class PaymentTypeMap(Base):
    __tablename__ = "payment_type"

    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)

