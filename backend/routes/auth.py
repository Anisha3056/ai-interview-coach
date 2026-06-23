from fastapi import APIRouter
from sqlalchemy.orm import Session

from models.auth import RegisterRequest, LoginRequest
from models.user import User

from services.auth_service import (
    ALGORITHM, hash_password, verify_password, create_access_token, verify_token
)

from database.db import SessionLocal
from fastapi import HTTPException
from fastapi import Header

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
    
@router.post("/login")
def login_user(
    request: LoginRequest
):

    db = SessionLocal()

    user = db.query(User).filter(
        User.email == request.email
    ).first()

    if not user:

        raise HTTPException(
    status_code=401,
    detail="Invalid email or password"
)

    if not verify_password(
        request.password,
        user.password_hash
    ):

        raise HTTPException(
    status_code=401,
    detail="Invalid email or password"
)
    token = create_access_token(
        {
            "sub":
            user.email
        }
    )

    return {
        "access_token":
        token,

        "token_type":
        "bearer"
    }
    
@router.get("/me")
def get_current_user(
    authorization: str = Header(None)
):

    if not authorization:

        return {
            "message":
            "Token missing"
        }

    token = authorization.replace(
        "Bearer ",
        ""
    )

    email = verify_token(token)

    if not email:

        return {
            "message":
            "Invalid token"
        }

    return {
        "email":
        email
    }
    
