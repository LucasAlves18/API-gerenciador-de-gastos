from sqlalchemy.orm import Session

from infrastructure.models.expense_map import ExpenseMap
from schemas.expense_schema import ExpenseCreate


class ExpenseRepository:
    def __init__(self, db: Session):
        self.db = db


    def create_expense(self, body: ExpenseCreate) -> type[ExpenseMap] | None:
        instance = ExpenseMap
        instance.id_payment_type = body.id_payment_type
        instance.value = body.value
        instance.description = body.description

        self.db.add(instance)
        self.db.commit()

        self.db.refresh(instance)

        return instance
