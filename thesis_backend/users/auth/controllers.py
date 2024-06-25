from typing import Annotated
from urllib import response
from fastapi import APIRouter, Depends, Request
from fastapi.security import OAuth2PasswordRequestForm
from .schemas import CreateLoginSchema, CreateUserSchema, BaseUserAccountSchema
from .presenter import UserPresenter, TokenPresenter
from .deps import get_option_presenter, response_data, get_token_service_data
from sqlalchemy.ext.asyncio import  AsyncSession

auth_controllers = APIRouter(prefix='/auth', tags=['users'])


@auth_controllers.post(**response_data.get('signup'))
async def sign_up(
        users_data: CreateUserSchema,
        option_presenter=Depends(get_option_presenter),
):
    return await UserPresenter(**option_presenter) \
        .sign_up(**users_data.dict())



@auth_controllers.post(**response_data.get('login'))
async def login(
        form_data: CreateLoginSchema,
       # form_data: OAuth2PasswordRequestForm = Depends(),
        option_presenter=Depends(get_option_presenter),
):
    #breakpoint()
    return await UserPresenter(**option_presenter) \
        .login(username=form_data.username, password=form_data.password)

# @auth_controllers.post('/logout')
# async def logout(request: Request):
#     response.delete_cookie("session_token")
#     return {"message": "Logged out successfully"}

@auth_controllers.post(**response_data.get('create_token'))
async def get_token(
        username: BaseUserAccountSchema,
        token_data=Depends(get_token_service_data)
):
    return await TokenPresenter(**token_data) \
        .get_token(username=username.username)

@auth_controllers.delete(**response_data.get('delete_user'))
async def delete_user(
        utilisateur_id : int,
        option_presenter=Depends(get_option_presenter)
      
):
    return await UserPresenter(**option_presenter) \
        .delete_user(utilisateur_id=utilisateur_id)

# @auth_controllers.post('/logout')
# async def logout(token: str = Depends(oauth2_scheme), option_presenter=Depends(get_option_presenter)):
#     return await UserPresenter(**option_presenter).logout(token)