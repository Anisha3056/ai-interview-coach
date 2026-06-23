from passlib.hash import pbkdf2_sha256
from jose import jwt
from datetime import datetime, timedelta
from jose import JWTError


SECRET_KEY = "super-secret-key"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 60

def hash_password(password):

    return pbkdf2_sha256.hash(password)


def verify_password(plain_password,hashed_password):

    return pbkdf2_sha256.verify(
        plain_password,
        hashed_password
    )
    


def create_access_token(data):

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update(
        {"exp": expire}
    )

    return jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
    
def verify_token(token):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        email = payload.get("sub")

        return email

    except JWTError:

        return None