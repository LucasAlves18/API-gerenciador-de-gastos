from sqlalchemy.orm import Session
from repository.user_repository import UserRepository
from schemas.user_schema import UserCreate, UserSearchResponse
from services.auth_service import pwd_context


class UserServices:
    def __init__(self, db:Session):
        self.db = db

    def create_user(self, request: UserCreate):
        verify_email = UserRepository(self.db).get_by_email(request.email)
        if verify_email:
            raise ValueError('Email já cadastrado no sistema!')

        hash_password = pwd_context.hash(request.password)
        UserRepository(self.db).create_user(request.name, request.email, hash_password, request.balance)
        return 'Conta criada com sucesso'

    def search_user(self, email: str):
        user = UserRepository(self.db).get_by_email(email)

        if not user:
            raise ValueError('Usuário não encontrado')

        user_response = UserSearchResponse(
            id=user.id,
            name=user.name,
            email=user.email,
            balance=user.balance
        )

        return user_response
