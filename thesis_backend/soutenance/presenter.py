from dataclasses import dataclass
from typing import List
from .schemas import CreateThesisSchema
from .interfaces.repositories_interface import \
     ThesisRepositoriesInterface
    
from .exceptions import ThesisExceptions
from sqlalchemy.ext.asyncio import AsyncSession


@dataclass
class ThesisPresenter:
    repository: ThesisRepositoriesInterface
    
    # async def create_thesis(self, thesis_data: CreateThesisSchema, db: AsyncSession):
    #     thesis_id = await self.repository.create_thesis(thesis_data, db)
    #     return {'thesis_id': thesis_id}
    async def create_thesis(self, thesis_data: CreateThesisSchema, matricules: list, db):
        thesis_id = await self.repository.create_thesis(thesis_data, matricules, db)
        return thesis_id