from sqlalchemy.orm import Session

from repository.expense_type_repository import ExpenseTypeRepository
from schemas.expense_type_schema import ExpenseTypeCreate


class ExpenseTypeService:
    def __init__(self, db: Session):
        self.db = db

    def create_expense_type(self, body: ExpenseTypeCreate):
        create = ExpenseTypeRepository(self.db).create_expense_type(body.description)

        if not create:
            raise ValueError('Não foi possível inserir novo registro!')

        return 'Tipo de pagamento criado com sucesso!'

