from sqlalchemy.orm import Session

from infrastructure.models.payment_type_map import PaymentTypeMap


class PaymentTypeRepository:
    def __init__(self, db: Session):
        self.db = db

    def search_payment_type_id(self, payment_type_id: int | None):
        query = self.db.query(PaymentTypeMap)

        if payment_type_id is not None:
            query = query.filter(PaymentTypeMap.id == payment_type_id)

        return query.all()

    def create_payment_type(self, description: str):
        instance = PaymentTypeMap()
        instance.description = description

        self.db.add(instance)
        self.db.commit()
        self.db.refresh(instance)
