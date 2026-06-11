from sqlalchemy.orm import Session
from infrastructure.models.user_map import UserMap

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_email(self, email: str) -> type[UserMap] | None:
        return self.db.query(UserMap).filter(UserMap.email == email).first()

    def create_user(self, name: str, email: str, password: str, balance: float):
        instance = UserMap()
        instance.name = name
        instance.email = email
        instance.password = password
        instance.balance = balance

        self.db.add(instance)
        self.db.commit()
        self.db.refresh(instance)

        return instance
