from sqlalchemy.orm import Session
from authentication.jwt import create_token
from repository.user_repository import UserRepository
from schemas.user_schema import UserLogin
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Auth:
    @staticmethod
    def login(db: Session, request: UserLogin):
        user = UserRepository(db).get_by_email(request.email)

        if not user:
            raise ValueError('Usuário ou senha incorreta')

        if not pwd_context.verify(request.password, user.password):
            raise ValueError('Usuário ou senha incorreta')

        token = create_token({"sub": str(user.id), "email": user.email})
        return {"access_token": token, "token_type": "bearer"}
