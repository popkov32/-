'''
Задача "Имитация работы с БД":
Создайте новое приложение FastAPI и сделайте CRUD запросы.
Создайте словарь users = {'1': 'Имя: Example, возраст: 18'}
Реализуйте 4 CRUD запроса:
get запрос по маршруту '/users', который возвращает словарь users.
post запрос по маршруту '/user/{username}/{age}', который добавляет в словарь по
максимальному по значению ключом значение строки "Имя: {username}, возраст: {age}".
И возвращает строку "User <user_id> is registered".
put запрос по маршруту '/user/{user_id}/{username}/{age}', который обновляет значение
 из словаря users под ключом user_id на строку "Имя: {username}, возраст: {age}". И возвращает
 строку "The user <user_id> is updated"
delete запрос по маршруту '/user/{user_id}', который удаляет из словаря users по ключу user_id
пару.
'''

from fastapi import FastAPI, Path, HTTPException
from typing import Annotated


app = FastAPI()

# импровизированная БД
users = {'1': 'Имя: Example, возраст: 18'}

# get-запрос, возвращаюший словарь users
@app.get("/users")
async def get_all_messages() -> dict:
    return users

#post-запрос, добавляющий в словарь нового пользователя
@app.post("/user/{user_name}/{age}")
async def create_user(
        user_name:
        Annotated[str, Path(min_length=5,
                            max_length=20,
                            description="Enter username",
                            example="Alexandr")],
        age:
        Annotated[int,Path(ge=18,
                           le=120,
                           description="Enter age",
                           example=55)]) -> dict:
    new_id = str(int(max(users, key=int)) + 1)
    new_user = f"Имя: {user_name}, возраст: {age}"
    users[new_id] = new_user
    #users.update({new_id: f'Имя: {user_name}, возраст: {age}'})
    return f"User {new_id} is registered"

#put-запрос, обновляющий значение из словаря users под ключом user_id
@app.put("/user/{user_id}/{user_name}/{age}")
async def update_user(
        user_name:
        Annotated[str, Path(min_length=5,
                            max_length=20,
                            description="Enter username",
                            example="Alexandr")],
        age:
        Annotated[int, Path(ge=18,
                            le=120,
                            description="Enter age",
                            example=55)],
        user_id: int = Path(ge=0)) -> dict:
    users[user_id] = f"Имя: {user_name}, возраст: {age}"
    return f"The user {user_id} has been updated"

# delete-запрос, удаляющий из словаря users по ключу user_id запись о пользователе
@app.delete("/user/{user_id}")
async def delete_user(user_id: str = Path(...)):
    if user_id in users:
        users.pop(user_id)
        return f"User {user_id} has been deleted"
    else:
        raise HTTPException(status_code=404, detail="The user was not found.")

#uvicorn module_16_3:app --reload