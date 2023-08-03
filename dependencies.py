from datetime import datetime, timedelta

import edgedb
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials
from jose import jwt
from jose.exceptions import JOSEError

import settings
from hashing_password import verify_password
from queries.get_user_by_username_async_edgeql import get_user_by_username
from schemas.token_schema import TokenData
from settings import setting_object

client = edgedb.create_async_client()


async def get_user(username: str):
    user_info = await get_user_by_username(client, arg0=username)
    if user_info:
        return user_info


async def authenticate_user(username: str, password: str):
    user = await get_user(username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode,
        setting_object.SECRET_KEY,
        algorithm=setting_object.ALGORITHM,
    )
    return encoded_jwt


async def has_access(
    credentials: HTTPAuthorizationCredentials = Depends(settings.security),
):
    token = credentials.credentials

    try:
        payload = jwt.decode(
            token,
            key=setting_object.SECRET_KEY,
            options={
                "verify_signature": False,
                "verify_aud": False,
                "verify_iss": False,
            },
        )
        username: str = payload.get("sub")
        if username is None:
            raise setting_object.credentials_exception
        token_data = TokenData(username=username)
    except JOSEError as e:
        raise HTTPException(status_code=401, detail=str(e))
    user = await get_user(username=str(token_data.username))
    if user is None:
        raise setting_object.credentials_exception
    if user.admin is False:
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Your are not an admin",
        )
    return user
