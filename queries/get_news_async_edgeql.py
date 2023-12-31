# AUTOGENERATED FROM 'queries/get_news.edgeql' WITH:
#     $ edgedb-py


from __future__ import annotations

import dataclasses
import datetime
import uuid

import edgedb


class NoPydanticValidation:
    @classmethod
    def __get_validators__(cls):
        from pydantic.dataclasses import dataclass as pydantic_dataclass

        pydantic_dataclass(cls)
        cls.__pydantic_model__.__get_validators__ = lambda: []
        return []


@dataclasses.dataclass
class GetNewsResult(NoPydanticValidation):
    id: uuid.UUID
    title: str
    date_published: datetime.date
    author: GetNewsResultAuthor
    section: str
    country: str
    news_content: str


@dataclasses.dataclass
class GetNewsResultAuthor(NoPydanticValidation):
    id: uuid.UUID


async def get_news(
    executor: edgedb.AsyncIOExecutor,
) -> list[GetNewsResult]:
    return await executor.query(
        """\
        # selectNews.edgeql

        select News {
          title,
          date_published,
          author,
          section,
          country,
          news_content
        };\
        """,
    )
