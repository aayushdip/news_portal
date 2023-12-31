# AUTOGENERATED FROM 'queries/get_subscriber_list.edgeql' WITH:
#     $ edgedb-py


from __future__ import annotations

import dataclasses
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
class GetSubscriberListResult(NoPydanticValidation):
    id: uuid.UUID
    name: str
    email: str
    username: str
    admin: bool
    subscriber: bool


async def get_subscriber_list(
    executor: edgedb.AsyncIOExecutor,
) -> list[GetSubscriberListResult]:
    return await executor.query(
        """\
        select User {
          name,
          email,
          username,
          admin,
          subscriber,
        } filter .subscriber = true\
        """,
    )
