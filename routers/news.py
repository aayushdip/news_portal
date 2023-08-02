from uuid import UUID

import edgedb
from fastapi import APIRouter, HTTPException, status

from queries import create_news_async_edgeql as create_news_qry
from queries import delete_news_async_edgeql as delete_news_qry
from queries import get_news_async_edgeql as get_news_qry
from queries import update_news_async_edgeql as update_news_qry
from responses_list.success_response import success_res
from schemas.news_schema import News

router = APIRouter()
client = edgedb.create_async_client()


@router.get("/news")
async def get_news() -> get_news_qry.GetNewsResult:
    news = await get_news_qry.get_news(client)
    return success_res(True, status.HTTP_200_OK, "Success", {"data": news})


@router.post("/news", status_code=status.HTTP_201_CREATED)
async def create_news_endpoint(news: News) -> create_news_qry.CreateNewsResult:
    try:
        created_news = await create_news_qry.create_news(
            client,
            title=news.title,
            date_published=news.date_published,
            author=news.author,
            section=news.section,
            country=news.country,
            news_content=news.news_content,
        )
    except edgedb.errors.ConstraintViolationError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"error": "Failed to create news entry."},
        )
    return success_res(
        True, status.HTTP_201_CREATED, "News created", {"data": created_news}
    )


@router.put("/news/{news_id}")
async def update_news(news_id: UUID, news: News):
    try:
        updated_news = await update_news_qry.update_news(
            client,
            news_id=news_id,
            title=news.title,
            date_published=news.date_published,
            author=news.author,
            section=news.section,
            country=news.country,
            news_content=news.news_content,
        )
    except edgedb.errors.ConstraintViolationError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"error": "Failed to update news entry."},
        )
    return success_res(
        True,
        status.HTTP_200_OK,
        "News updated",
        {"data": updated_news},
    )


@router.delete("/news/{news_id}")
async def delete_news(news_id: UUID) -> delete_news_qry.DeleteNewsResult:
    try:
        deleted_news = await delete_news_qry.delete_news(
            client,
            news_id=news_id,
        )
    except edgedb.errors.ConstraintViolationError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"error": "News entry not found."},
        )
    return success_res(
        True,
        status.HTTP_200_OK,
        "News deleted",
        {"data": deleted_news},
    )
