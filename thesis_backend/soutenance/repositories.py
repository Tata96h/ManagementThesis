from dataclasses import dataclass
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession, AsyncResult
from sqlalchemy import select, insert, delete, update
from sqlalchemy.orm import subqueryload

from users.auth.models import Etudiant, Users
from users.etudiants.schemas import CreateEtudiantSchema
from .schemas import CreateThesisSchema, CreateThesisSchema
from .models import  Appartenir, Thesis
from .exceptions import ThesisExceptions
from .interfaces.repositories_interface import \
    ThesisRepositoriesInterface
from sqlalchemy import exists

@dataclass
class ThesisRepositories(ThesisRepositoriesInterface):
    session: AsyncSession

    async def create_thesis(self, thesis_data: CreateThesisSchema, matricules: list, session: AsyncSession):
        try:
            thesis_dict = thesis_data.dict(exclude_unset=True)
            thesis_stmt = insert(Thesis).values(**thesis_dict).returning(Thesis.id)
            result = await session.execute(thesis_stmt)
            thesis_id = result.scalar()
            print(f"Soutenance créée avec succès, ID: {thesis_id}")

            etudiant_ids = await self.get_etudiant_ids(session, matricules)
            print(etudiant_ids)

            # Vérifier si tous les matricules ont des IDs valides
            if any(etudiant_id is None for etudiant_id in etudiant_ids.values()):
                raise ThesisExceptions("Un ou plusieurs matricules sont invalides.")

            for matricule, etudiant_id in etudiant_ids.items():
                # Vérifier si l'étudiant est déjà associé à une autre thèse
                appartenir_exist = await session.execute(
                    select(exists().where(Appartenir.etudiant_id == etudiant_id))
                )
                if appartenir_exist.scalar():
                    raise ThesisExceptions(f"L'étudiant avec le matricule {matricule} est déjà associé à une autre thèse.")

                appartenir_stmt = insert(Appartenir).values(etudiant_id=etudiant_id, soutenance_id=thesis_id)
                await session.execute(appartenir_stmt)

            await session.commit()
            print("La thèse et les associations ont été créées avec succès.")
            return thesis_id

        except Exception as e:
            print(f"Une erreur s'est produite : {str(e)}")
            await session.rollback()
            raise e


    async def get_etudiant_ids(self, session, matricules: list[str]):
        stmt = (
            select(Etudiant.id, Etudiant.matricule)
            .where(Etudiant.matricule.in_(matricules))
            .order_by(Etudiant.matricule)
        )
        result = await session.execute(stmt)
        etudiant_ids = {row.matricule: row.id for row in result}
        return etudiant_ids
    
    