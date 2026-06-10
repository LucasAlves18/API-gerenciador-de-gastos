from fastapi import HTTPException
from sqlalchemy.orm import Session
from authentication.jwt import create_token
from repository.user_repository import UserRepository
from schemas.user import UserLogin


class Auth:
    @staticmethod
    def login(db: Session, request: UserLogin):
        user = UserRepository(db).get_by_email(request.email)

        if not user:
            raise HTTPException(status_code=404, detail='Usuário ou senha incorreta')

        if user.senha != request.password:
            raise HTTPException(status_code=404, detail='Usuário ou senha incorreta')

        token = create_token({"sub": str(user.id), "email": user.email})
        return {"access_token": token, "token_type": "bearer"}