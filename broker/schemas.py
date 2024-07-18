from pydantic import BaseModel, EmailStr


class EmailSchema(BaseModel):
    email: list[EmailStr]
