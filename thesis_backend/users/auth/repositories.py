
from sqlalchemy import select, insert, delete, update
from users.auth.exceptions import AuthExceptions
from .interfaces.repositories_interface import UserRepositoriesInterface
from dataclasses import dataclass
from sqlalchemy.ext.asyncio import AsyncSession

from .models import Users


@dataclass
class UserRepositories(UserRepositoriesInterface):
    session: AsyncSession

    async def save_user(self, username: str, email: str, password: str, nom: str, prenoms: str, role_id: int) -> int:
        stmt = insert(Users).values(
            email=email,
            username=username,
            password=password,
            nom=nom,
            prenoms=prenoms,
            role_id=role_id
        ).returning(Users.id)
        result = await self.session.execute(statement=stmt)
        await self.session.commit()
        utilisateur_id = result.scalar_one()
        return utilisateur_id

    async def receive_user_by_username(self, username: str):
        stmt = select(Users).where(Users.username == username)
        result = await self.session.execute(statement=stmt)
        return result.scalars().first()
    

    async def delete_user(self, utilisateur_id: int):
        stmt = delete(Users).where(Users.id == utilisateur_id)
        await self.session.execute(stmt)
        await self.session.commit()
    # async def save_token(self, token: str) -> None:
    #     stmt = insert(Token).values(token=token)
    #     await self.session.execute(statement=stmt)
    #     await self.session.commit()

    # async def deactivate_token(self, token: str) -> None:
    #     stmt = update(Token).where(Token.token == token).values(is_active=False)
    #     await self.session.execute(statement=stmt)
    #     await self.session.commit()

    # async def is_token_active(self, token: str) -> bool:
    #     stmt = select(Token).where(Token.token == token)
    #     result = await self.session.execute(statement=stmt)
    #     token_record = result.scalars().first()
    #     return token_record and token_record.is_active