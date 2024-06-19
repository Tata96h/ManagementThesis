from typing import List, Optional
from pydantic import BaseModel, EmailStr, Field, validator
from datetime import datetime

from users.auth.schemas import UsersSchema
from users.profile.schemas import UserSchema


class CreateEtudiantSchema(BaseModel):
    username: str
    password: str
    email: str
    nom: str
    prenoms: str
    matricule: str
    filiere_id: int
    
    

class UpdateEtudiantSchema(BaseModel):
    matricule: str | None = Field(None, max_length=200)
    filiere_id: int | None
   

    @property
    def is_empty(self): return not self.dict(exclude_none=True)


class EtudiantSchema(BaseModel):
    id: int
    matricule: str
    slug: Optional[str]
    utilisateur_id: int
    filiere_id: int
    created: datetime
    utilisateur: UsersSchema

    class Config:
        from_attributes = True

class FiliereSchema(BaseModel):
    id: int
    nom: str
    departement_id: int

    class Config:
        from_attributes = True


class EmailSchema(BaseModel):
    email: List[EmailStr]

    class Config:
        from_attributes = True
    