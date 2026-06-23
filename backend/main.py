from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from database.db import engine
from database.db import Base
from models.user import User
from models.interview_sessions import InterviewSession
    


from routes.resume import (
    router as resume_router
)

from routes.interview import (
    router as interview_router
)

from routes.auth import (
    router as auth_router
)

app = FastAPI()
Base.metadata.create_all(bind=engine)

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

app.include_router(
    auth_router,
    prefix="/auth",
    tags=["auth"]
)

@app.get("/")
async def home():
    return {
        "message": "AI Interview Coach API is running 🚀"
    }