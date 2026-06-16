from pydantic import BaseModel, field_validator


class ExpenseCreate(BaseModel):
    id_acount: int
    id_payment_type: int
    value: float
    description: str
