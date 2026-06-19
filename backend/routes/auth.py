from fastapi import APIRouter
from sqlalchemy.orm import Session

from models.auth import RegisterRequest
from models.user import User

from services.auth_service import (
    hash_password
)

from database.db import SessionLocal
from fastapi import HTTPException

router = APIRouter()


@router.post("/register")
def register_user(
    request: RegisterRequest
):

    db: Session = SessionLocal()

    existing_user = db.query(User).filter(
        User.email == request.email
    ).first()

    if existing_user:

        raise HTTPException(
    status_code=400,
    detail="Email already registered"
)

    user = User(
        name=request.name,
        email=request.email,
        password_hash=
        hash_password(
            request.password
        )
    )

    db.add(user)

    db.commit()

    return {
        "message":
        "User registered successfully"
    }