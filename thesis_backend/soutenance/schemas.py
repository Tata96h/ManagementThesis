from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime

# from users.etudiants.schemas import EtudiantSchema
from users.profile.schemas import UserSchema


class CreateThesisSchema(BaseModel):
    numero: str
    theme: Optional[str] = Field(None, max_length=200)
    lieu_stage: Optional[str] = Field(None, max_length=200)
    responsable: Optional[str] = Field(None, max_length=200)
    cahier_charge: Optional[str] = Field(None, max_length=255)
    choix1_id: Optional[int] = None
    choix2_id: Optional[int] = None
    maitre_memoire: Optional[int] = None
    annee_id: Optional[int] = None
    
    


class UpdateThesisSchema(BaseModel):
    numero: str
    theme: str | None = Field(max_length=200)
    lieu_stage: str | None = Field(max_length=200)
    responsable: str | None = Field(max_length=200)
    cahier_charge: str | None = Field(None, max_length=255)
    choix1_id: int | None
    choix2_id: int | None
    maitre_memoire: int | None

    @property
    def is_empty(self):
        return not self.dict(exclude_none=True)

class ThesisSchema(CreateThesisSchema):
    id: int
    created: datetime
    updated: datetime

    class Config:
        from_attributes = True

class AppartenirSchema(BaseModel):
    id: int
    etudiant_id: int
    soutenance_id: int

    class Config:
        from_attributes = True