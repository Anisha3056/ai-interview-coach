from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from routes.resume import (
    router as resume_router
)

from routes.interview import (
    router as interview_router
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://localhost:5173"
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