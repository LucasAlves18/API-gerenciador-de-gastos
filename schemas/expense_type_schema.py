from pydantic import BaseModel, field_validator


class ExpenseTypeCreate(BaseModel):
    description: str

    @field_validator("description")
    def name_not_empty(cls, v):
            if len(v) < 1:
                raise ValueError("Nome não pode ser vazio")
            return v
