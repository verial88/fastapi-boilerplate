from pydantic import BaseModel, EmailStr

from src.core.schemas import OutputApiSchema


class UserSchema(BaseModel):
    email: EmailStr
    username: str
    last_name: str
    first_name: str
    is_active: bool = True
    is_superuser: bool = False


class UserResponseSchema(OutputApiSchema):
    email: EmailStr
    username: str
    last_name: str
    first_name: str
    is_active: bool = True
    is_superuser: bool = False
