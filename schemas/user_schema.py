from pydantic import BaseModel, EmailStr, field_validator


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserCreate(BaseModel):
    name: str
    password: str
    email: EmailStr
    balance: float

    @field_validator("name")
    def name_not_empty(cls, v):
        if len(v) < 1:
            raise ValueError("Nome não pode ser vazio")
        return v

    @field_validator("password")
    def password_min_length(cls, v):
        if len(v) < 8:
            raise ValueError("Senha muito curta")
        return v

    @field_validator("balance")
    def balance_not_negative(cls, v):
        if v < 0:
            raise ValueError("Saldo não pode ser negativo")
        return v

    @field_validator("password")
    def password_max_length(cls, v):
        if len(v.encode("utf-8")) > 72:
            raise ValueError("Senha muito longa")
        return v

class UserSearchResponse(BaseModel):
    id: int | None
    name: str | None
    email: str | None
    balance: float | None


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"