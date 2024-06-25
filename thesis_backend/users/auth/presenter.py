from dataclasses import dataclass

from database import AsyncSessionLocal

from users.auth.repositories import UserRepositories
from users.enseignants.interfaces.repositories_interface import EnseignantRepositoriesInterface
from users.enseignants.schemas import CreateEnseignantSchema
from users.etudiants.interfaces.repositories_interface import EtudiantRepositoriesInterface
from users.etudiants.schemas import CreateEtudiantSchema
from .interfaces.repositories_interface import UserRepositoriesInterface
from .interfaces.password_service_interface import PasswordServiceInterface
from .interfaces.token_service_interface import TokenServiceInterface
from .exceptions import AuthExceptions
from .mixins import CreateTokenMixin
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import  AsyncSession




@dataclass
class TokenPresenter(CreateTokenMixin):
    token_service: TokenServiceInterface

    async def get_token(self, username: str) -> dict:
        return await self.create_token(
            username=username, token_service=self.token_service)

    
    
@dataclass
class UserPresenter(CreateTokenMixin):
    repository: UserRepositoriesInterface
    etudiant_repository:EtudiantRepositoriesInterface
    enseignant_repository:EnseignantRepositoriesInterface
    password_service: PasswordServiceInterface
    token_service: TokenServiceInterface

   
    async def __check(self, username: str, password: str):
        if not (user := await self.repository.receive_user_by_username(
                username=username)) or \
                not await self.password_service.verify_password(
                    plain_password=password,
                    hashed_password=user.password):
            raise AuthExceptions().incorrect_username_or_password
        return user


    async def login(self, username: str, password: str):
        user = await self.__check(username=username, password=password)

        # Vérifier si l'utilisateur est actif
        if not user.is_active:
            raise AuthExceptions().UNAUTHORIZED

        # Si l'utilisateur est actif, créer le jeton
        token_data = await self.create_token(
        username=user.username, token_service=self.token_service
        )

        # Retourner le token et les informations utilisateur
        return {
            'access_token': token_data['access_token'],
            'token_type': token_data['token_type'],
            'user_info': {
                'utilisateur_id': user.id,
                'nom': user.nom,
                'prenoms': user.prenoms,
                'role': user.role_id,
                'admin': user.is_admin
        }
    }
    

    async def sign_up(self, username: str, email:str, password: str, nom: str ,prenoms: str, role_id: int):
        if await self.repository.receive_user_by_username(username=username):
            raise AuthExceptions().username_exists
        _password = await self.password_service \
            .hashed_password(password=password)
        await self.repository.save_user(username=username, email=email, password=_password, nom=nom, prenoms=prenoms, role_id=role_id)
        raise AuthExceptions().user_create

    async def delete_user(self, utilisateur_id: int):
        return await self.repository.delete_user(utilisateur_id=utilisateur_id)

    
# async def logout(self, token: str):
#         await self.repository.deactivate_token(token)
#         return {"msg": "Successfully logged out"}
