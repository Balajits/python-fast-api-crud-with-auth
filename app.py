from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.database import engine
from database.db_base import Base
from api import User
from api import Task
import uvicorn

app = FastAPI(title="My App", description="Hello World", version="0.1")

origins = ["*"]
Base.metadata.create_all(bind=engine)


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(User.router)
app.include_router(Task.router)

if __name__ == "__main__":
    uvicorn.run(app, port=1996)