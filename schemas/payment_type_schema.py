from pydantic import BaseModel, field_validator


class SearchPaymentTypeResponse(BaseModel):
    id: int
    description: str


class CreatePaymentType(BaseModel):
    description: str

    @field_validator("description")
    def password_min_length(cls, v):
        if len(v) < 1:
            raise ValueError("Senha muito curta")
        return v
