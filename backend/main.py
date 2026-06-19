from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from database.db import engine
from database.db import Base
from models.user import User

from routes.resume import (
    router as resume_router
)

from routes.interview import (
    router as interview_router
)

app = FastAPI()
Base.metadata.create_all(bind=engine)

from sqlalchemy import inspect

inspector = inspect(engine)

print("Tables in DB:",
      inspector.get_table_names())
print(Base.metadata.tables.keys())
app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
        "https://ai-interview-coach-self.vercel.app"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)

app.include_router(
    resume_router,
    prefix="/resume",
    tags=["resume"]
)

app.include_router(
    interview_router,
    prefix="/interview",
    tags=["interview"]
)

@app.get("/")
async def home():
    return {
        "message": "AI Interview Coach API is running 🚀"
    }