import edgedb
from fastapi import APIRouter, HTTPException, Query, status

from hashing_password import hash_password
from queries import create_user_async_edgeql as create_user_qry
from queries import get_subscriber_list_async_edgeql as get_user_subscriber_qry
from queries import get_user_by_username_async_edgeql
from queries import get_users_async_edgeql as get_user_all_list_qry
from responses_list.success_response import success_res
from schemas.user_schema import UserCreate

router = APIRouter()
client = edgedb.create_async_client()


@router.get("/users")
async def get_users(username: str = Query(None, max_length=50)):
    if not username:
        users = await get_user_all_list_qry.get_users(client)
        return success_res(
            True,
            status.HTTP_200_OK,
            "Success",
            {"data": users},
        )
    else:
        user = await get_user_by_username_async_edgeql.get_user_by_username(
            client, arg0=username
        )
        return success_res(
            True,
            status.HTTP_200_OK,
            "Success",
            {"data": user},
        )


@router.get("/subscribers")
async def get_subscribers():
    subscribers = await get_user_subscriber_qry.get_subscriber_list(client)
    return success_res(
        True,
        status.HTTP_200_OK,
        "Success",
        {"data": subscribers},
    )


@router.post("/users", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate):
    try:
        created_user = await create_user_qry.create_user(
            client,
            name=user.name,
            email=user.email,
            username=user.username,
            admin=user.admin,
            subscriber=user.subscriber,
            hashed_password=hash_password(user.hashed_password),
        )
    except edgedb.errors.ConstraintViolationError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"error": f"Username '{user.name}' already exists."},
        )
    return success_res(
        True,
        status.HTTP_201_CREATED,
        "Success",
        {"data": created_user},
    )
