from typing import List
from fastapi import APIRouter, Body, Depends, HTTPException, Query

from database import get_db_session
from users.auth.deps import get_user
from users.etudiants.schemas import CreateEtudiantSchema
from .presenter import  ThesisPresenter
from .schemas import CreateThesisSchema
from sqlalchemy.ext.asyncio import AsyncSession
from .deps import response_data, get_user, get_presenter, \
    get_slug_user, get_thesis_user, get_limit_offset_user, \
    get_create_data_user, get_updated_data_slug_user

thesis_controllers = APIRouter(prefix='/thesis', tags=['thesis'])


@thesis_controllers.post(**response_data.get('create_thesis'))
async def create_thesis(
        thesis_data: CreateThesisSchema,
        matricules: str,  # Les matricules sont envoyés en tant que chaîne, séparés par des virgules
        presenter: ThesisPresenter = Depends(get_presenter),
        db: AsyncSession = Depends(get_db_session)
    ):
    try:
        matricules_list = [m.strip() for m in matricules.split(',')]
        thesis_id = await presenter.create_thesis(thesis_data, matricules_list, db)
        return {"thesis_id": thesis_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))




# async def create_thesis(
#     thesis_data: CreateThesisSchema,
#     user=Depends(get_user),
#     presenter: ThesisPresenter = Depends(get_presenter),
#     db: AsyncSession = Depends(get_db_session)
# ):
#     return await presenter.create_thesis(thesis_data, db)
