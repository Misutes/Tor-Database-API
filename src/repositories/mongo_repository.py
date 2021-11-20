from typing import Any, List

from models import UpdateUsersData, User


class TorRepository:
    def __init__(self, db):
        self._db = db

    async def creat_users(self, users: List[User]):
        await self._db.insert_many([user.dict() for user in users])

    async def get_users(
        self, fields: List[str], where_name: str, where_value: Any, count: int
    ):
        result = (
            self._db.find(
                {where_name: {"$eq": where_value}}, {field: 1 for field in fields}
            )
            if fields
            else self._db.find({where_name: {"$eq": where_value}})
        )
        return [user for user in await result.to_list(length=count)]

    async def update_users(self, update_data: UpdateUsersData):
        await self._db.update_many(
            {update_data.where_field: {"$eq": update_data.where_value}},
            {"$set": {update_data.field_name: update_data.field_value}},
        )
