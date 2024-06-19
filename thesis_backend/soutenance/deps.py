from fastapi import status, Depends
from permissions import UserPermission
from users.auth.token_service import TokenService
from .schemas import ThesisSchema, CreateThesisSchema, UpdateThesisSchema
from .repositories import ThesisRepositories

from .presenter import ThesisPresenter
from database import get_db_session


async def get_user(
        user=Depends(UserPermission(token_service=TokenService())
                         .get_current_user)
):
    yield user


# async def get_repository_service(session=Depends(get_db_session)):
#     yield {
#         'repository': ChannelRepositories(session=session)
#     }


async def get_presenter(session=Depends(get_db_session)):
    presenter = ThesisPresenter(
        repository=ThesisRepositories(session=session))
    yield presenter


async def get_thesis_user(thesis_id: int, utilisateur_id: int) -> dict:
    return {'thesis_id': thesis_id, 'utilisateur_id': utilisateur_id}


async def get_limit_offset_user(user_id: int, limit: int, offset: int) -> dict:
    return {'utilisateur_id': user_id, 'limit': limit, 'offset': offset}


async def get_slug_user(thesis_slug: str, utilisateur_id: int) -> dict:
    return {'thesis_slug': thesis_slug, 'utilisateur_id': utilisateur_id}


async def get_updated_data_slug_user(updated_data: UpdateThesisSchema,
                                         thesis_slug: str,
                                         utilisateur_id: int) -> dict:
    return {
        'updated_data': updated_data,
        'thesis_slug': thesis_slug,
        'utilisateur_id': utilisateur_id
    }


async def get_create_data_user(utilisateur_id: int,
                                   thesis_data: CreateThesisSchema) -> dict:
    return {'utilisateur_id': utilisateur_id, 'thesis_data': thesis_data}


response_data = {
    
    
    
    'create_thesis': {
        'path': '/',
        'status_code': status.HTTP_201_CREATED,
    },
    
}
