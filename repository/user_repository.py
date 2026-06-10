from sqlalchemy.orm import Session
from infraestrutura.models.user_map import UserMap

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_email(self, email: str) -> type[UserMap] | None:
        return self.db.query(UserMap).filter(UserMap.email == email).first()
