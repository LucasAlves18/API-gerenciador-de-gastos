from sqlalchemy.orm import Session

from repository.payment_type_repository import PaymentTypeRepository
from schemas.payment_type_schema import SearchPaymentTypeResponse, CreatePaymentType


class PaymentTypeServices:
    def __init__(self, db: Session):
        self.db = db

    def search_payment_type(self, id: int | None):
        search = PaymentTypeRepository(self.db).search_payment_type_id(id)

        if not search:
            raise ValueError('Nenhum registro encontrado!')

        return [SearchPaymentTypeResponse(**search)]

    def create_payment_type(self, request: CreatePaymentType):
        PaymentTypeRepository(self.db).create_payment_type(request.description)
        return 'Metódo de pagamento criado!'
