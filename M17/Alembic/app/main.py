from fastapi import FastAPI
from routers import user, task

app = FastAPI()

app.get( '/' )


@app.get( '/' )
async def welcome():
    return {'message': 'Welcome to Taskmaneger'}


app.include_router( user.router )
app.include_router( task.router )

# uvicorn main:app --reload
