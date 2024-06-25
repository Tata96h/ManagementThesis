from abc import ABC, abstractmethod
<<<<<<< HEAD
from ..schemas import CreateThesisSchema

=======
from typing import Dict, List
from ..schemas import CreateThesisSchema, UpdateThesisSchema
from sqlalchemy.ext.asyncio import AsyncSession
>>>>>>> 72a4943caa0a8fe86e91703bd7adad3a3e137997

class ThesisRepositoriesInterface(ABC):

   

    @abstractmethod
    async def create_thesis(
            self, matricules: list,  thesis_data: CreateThesisSchema):
        pass

<<<<<<< HEAD
    
   
=======
    @abstractmethod
    async def get_thesis(self, utilisateur_id: int, years_id: int, limit: int, offset: int, db):
        pass

    @abstractmethod
    async def get_all_thesis(self, annee_id: int, limit: int, offset: int, db):
        pass
    
    @abstractmethod
    async def update_thesis(
            self, utlisateur_id: int, thesis_slug: str,
            updated_data: UpdateThesisSchema
    ):
        pass

    @abstractmethod
    async def get_thesisa(self, thesis_slug: str):
        pass
    
    @abstractmethod
    async def get_all_thesis_with_students(self, annee_id: int, limit: int, offset: int, db: AsyncSession):
        pass
>>>>>>> 72a4943caa0a8fe86e91703bd7adad3a3e137997
