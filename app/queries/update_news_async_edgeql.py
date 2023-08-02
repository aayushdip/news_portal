# AUTOGENERATED FROM 'queries/update_news.edgeql' WITH:
#     $ edgedb-py


from __future__ import annotations
import dataclasses
import datetime
import edgedb
import uuid


class NoPydanticValidation:
    @classmethod
    def __get_validators__(cls):
        from pydantic.dataclasses import dataclass as pydantic_dataclass
        pydantic_dataclass(cls)
        cls.__pydantic_model__.__get_validators__ = lambda: []
        return []


@dataclasses.dataclass
class UpdateNewsResult(NoPydanticValidation):
    id: uuid.UUID


async def update_news(
    executor: edgedb.AsyncIOExecutor,
    *,
    news_id: uuid.UUID,
    title: str,
    date_published: datetime.date,
    author: str,
    section: str,
    country: str,
    news_content: str,
) -> UpdateNewsResult | None:
    return await executor.query_single(
        """\
        UPDATE News
            FILTER .id = <uuid>$news_id
            SET {
                title := <str>$title,
                date_published := <cal::local_date>$date_published,
                author := <str>$author,
                section := <str>$section,
                country := <str>$country,
                news_content := <str>$news_content,
            }\
        """,
        news_id=news_id,
        title=title,
        date_published=date_published,
        author=author,
        section=section,
        country=country,
        news_content=news_content,
    )