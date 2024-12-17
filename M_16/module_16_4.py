# Задача "Модель пользователя":

from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

# импровизированная БД
users = []


# создание класса(модели):
class User( BaseModel ):
    id: int = None
    username: str
    age: int


# get-запрос, возвращаюший список users
@app.get( "/users", response_model=[] )
async def get_all_users() -> list:
    return users


# post-запрос, добавляющий в словарь нового пользователя
@app.post( "/user/{username}/{age}", response_model=str )
async def create_user(user: User,
                      username:
                      Annotated[str, Path( min_length=5,
                                           max_length=20,
                                           description="Enter username",
                                           example="Alexandr" )],
                      age:
                      Annotated[int, Path( ge=18,
                                           le=120,
                                           description="Enter age",
                                           example=55 )]) -> str:
    if users:
        new_id = max( user.id for user in users ) + 1
    else:
        new_id = 1
    user.id = new_id
    user.username = username
    user.age = age
    users.append( user )
    return f"User {new_id} is registered"


# put-запрос, обновляющий значение из словаря users под ключом user_id
@app.put( "/user/{user_id}/{username}/{age}", response_model=str )
async def update_user(user: User,
                      username:
                      Annotated[str, Path( min_length=5,
                                           max_length=20,
                                           description="Enter username",
                                           example="Alexandr" )],
                      age:
                      Annotated[int, Path( ge=18,
                                           le=120,
                                           description="Enter age",
                                           example=55 )],
                      user_id: int = Path( ge=0 )) -> str:
    for existing_user in users:
        if existing_user.id == user_id:
            existing_user.username = username
            existing_user.age = age
            return f"The user {user_id} has been updated"
    raise HTTPException( status_code=404, detail="The user was not found" )


# delete-запрос, удаляющий из словаря users по ключу user_id запись о пользователе
@app.delete( "/user/{user_id}", response_model=str )
async def delete_user(user_id: int = Path( ge=0 )) -> str:
    for i, existing_user in enumerate( users ):
        if existing_user.id == user_id:
            users.pop( i )
            return f"User {user_id} has been deleted"
    raise HTTPException( status_code=404, detail="The user was not found." )

# uvicorn module_16_4:app --reload
