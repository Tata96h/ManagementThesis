from typing import Optional
from pydantic import BaseModel, Field


class BaseUserAccountSchema(BaseModel):
    username: str = Field(max_length=200)


class CreateUserSchema(BaseUserAccountSchema):
    email: str
    password: str
    nom: str
    prenoms: str
    role_id: int


class CreateLoginSchema(BaseModel):
    username: str = Field(max_length=200)
    password: str

class TokenSchema(BaseModel):
    access_token: str
    token_type: str
    user_info: dict

    class Config:
        from_attributes = True

# Exemple de schéma pour les informations utilisateur
class UserInfoSchema(BaseModel):
    utilisateur_id: int
    nom: str
    prenoms: str
    role_id: int
    is_admin: str

    class Config:
        from_attributes = True

class UsersSchema(BaseModel):
    id: int
    username: str
    email: str
    nom: str
    prenoms: str
    bio: Optional[str]
    role_id: int
    is_active: bool
    is_admin: bool
    # created: str

    class Config:
        from_attributes = True

