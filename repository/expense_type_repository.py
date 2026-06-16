from sqlalchemy.orm import Session
from infrastructure.models.expense_type_map import ExpenseTypeMap


class ExpenseTypeRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_expense_type(self, description: str) -> ExpenseTypeMap:
        instance = ExpenseTypeMap()
        instance.description = description

        self.db.add(instance)
        self.db.commit()
        self.db.refresh(instance)

        return instance