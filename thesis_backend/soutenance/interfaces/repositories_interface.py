from abc import ABC, abstractmethod
from ..schemas import CreateThesisSchema


class ThesisRepositoriesInterface(ABC):

   

    @abstractmethod
    async def create_thesis(
            self, matricules: list,  thesis_data: CreateThesisSchema):
        pass

    
   