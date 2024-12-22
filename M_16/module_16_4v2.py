"""
Задача "Модель пользователя":

Подготовка:
Используйте CRUD запросы из предыдущей задачи.
Создайте пустой список users = []
Создайте класс(модель) User, наследованный от BaseModel, который будет содержать следующие поля:
id - номер пользователя (int)
username - имя пользователя (str)
age - возраст пользователя (int)

Измените и дополните ранее описанные 4 CRUD запроса:
get запрос по маршруту '/users' теперь возвращает список users.
post запрос по маршруту '/user/{username}/{age}', теперь:
Добавляет в список users объект User.
id этого объекта будет на 1 больше, чем у последнего в списке users. Если список users пустой, то 1.
Все остальные параметры объекта User - переданные в функцию username и age соответственно.
В конце возвращает созданного пользователя.
put запрос по маршруту '/user/{user_id}/{username}/{age}' теперь:
Обновляет username и age пользователя, если пользователь с таким user_id есть в списке users и возвращает его.
В случае отсутствия пользователя выбрасывается исключение HTTPException с описанием "User was not found" и кодом 404.
delete запрос по маршруту '/user/{user_id}', теперь:
Удаляет пользователя, если пользователь с таким user_id есть в списке users и возвращает его.
В случае отсутствия пользователя выбрасывается исключение HTTPException с описанием "User was not found" и кодом 404.
"""

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
async def get_all_users() -> list[User]:
    """
    Функция обработки запроса при обращении к странице с пользователями.
    :return: список с информацией о пользователях в базе.
    """
    return users


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
    # return f"User {new_id} is registered"
    # исправлено: вместо f-строки выводятся данные нового пользователя
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
            # return f"The user {user_id} has been updated"
            # исправлено: вместо f-строки выводятся данные обновленного пользователя
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

# uvicorn module_16_4:app --reload
