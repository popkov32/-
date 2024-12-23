"""

"""

from fastapi import FastAPI, Path, HTTPException, Request
from pydantic import BaseModel
from typing import Annotated, List
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

# импровизированная БД
users = []

#подключаем папку с шаблонами
templates = Jinja2Templates(directory='templates')

# создание класса(модели):
class User( BaseModel ):
    id: int = None
    username: str
    age: int

# get-запрос по маршруту'/':
@app.get('/')
async def get_main_page(request: Request) -> HTMLResponse:
    '''
    Функция обработки запроса при обращении к главной странице.
    :param request: Request
    :return: HTML страница на основе шаблона со списоком информации о пользователях в базе.
    '''
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})

# get-запрос, возвращаюший страницу конкретного пользователя:
@app.get( '/user/{user_id}' )
async def get_user(request: Request, user_id) -> HTMLResponse:
    """
    Функция обработки запроса при обращении к странице с пользователем.
    :return: страница на основе шаблона с информацией о конкретном пользователе из базы.
    """
    for existing_user in users:
        if existing_user.id == user_id:
            user = users[users.index(existing_user)]
            return templates.TemplateResponse('users.html', {'request': request,
                                                             'user': user})
    raise HTTPException( status_code=404, detail="The user was not found" )


# post-запрос, добавляющий в словарь нового пользователя
@app.post( "/user/{username}/{age}" )
async def create_user(username:
Annotated[str, Path( min_length=5,
                     max_length=20,
                     description="Enter username",
                     example="Alexandr" )],
                      age:
                      Annotated[int, Path( ge=18,
                                           le=120,
                                           description="Enter age",
                                           example=55 )]) -> User:
    """
    Функция обработки запроса добавления нового пользователя в базу.
    :param username: имя нового пользователя;
    :param age: возраст нового пользователя.
    :return: новый пользователь user.
    """
    if users:
        new_id = max( user.id for user in users ) + 1
    else:
        new_id = 1
    user = User( id=new_id, username=username, age=age )
    users.append( user )
    return user


# put-запрос, обновляющий значение из словаря users под ключом user_id
@app.put( "/user/{user_id}/{username}/{age}" )
async def update_user(user_id:
Annotated[int, Path( ge=1,
                     description="Enter User ID",
                     example=1 )],
                      username:
                      Annotated[str, Path( min_length=5,
                                           max_length=20,
                                           description="Enter username",
                                           example="Alexandr" )],
                      age:
                      Annotated[int, Path( ge=18,
                                           le=120,
                                           description="Enter age",
                                           example=55 )]
                      ) -> User:
    """
    Функция обработки запроса обновления сведений о пользователе в базе
    :param user_id: идентификатор обновляемого пользователя
    :param username: имя пользователя
    :param age: возраст пользователя
    :return: новые сведения о пользователе
    """
    for existing_user in users:
        if existing_user.id == user_id:
            existing_user.username = username
            existing_user.age = age
            return existing_user
    raise HTTPException( status_code=404, detail="The user was not found" )


# delete-запрос, удаляющий из словаря users по ключу user_id запись о пользователе
@app.delete( "/user/{user_id}" )
async def delete_user(user_id: int = Path( ge=0 )) -> User:
    """
    Функция обработки запроса удаления пользователя из базы.
    :param user_id: идентификатор удаляемого пользователя.
    :return: данные о удаленном пользователе.
    """
    for i, deleting_user in enumerate( users ):
        if deleting_user.id == user_id:
            users.pop( i )
            # return f"User {user_id} has been deleted"
            # исправлено: вместо f-строки выводятся данные удаленного пользователя
            return deleting_user
    raise HTTPException( status_code=404, detail="The user was not found." )

# uvicorn module_16_5:app --reload
