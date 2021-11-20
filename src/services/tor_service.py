from typing import Any, List, Optional

import inject

from models import UpdateUsersData, User
from repositories.mongo_repository import TorRepository
from utils.util import remove_file

service = None


@inject.autoparams()
def get_service(repo: TorRepository):
    global service
    if service is None:
        service = TorService(repo)
    return service


class TorService:
    @inject.autoparams()
    def __init__(self, repo: TorRepository):
        self._repo = repo

    async def creat_users(self, users: List[User]):
        await self._repo.creat_users(users)

    async def get_users(
        self, fields: Optional[List[str]], where_name: str, where_value: Any, count: int
    ):
        return await self._repo.get_users(fields, where_name, where_value, count)

    async def update_users(self, update_data: UpdateUsersData):
        await self._repo.update_users(update_data)

    async def get_file(self, path: str, fields: str, where_name: str, count: int):
        remove_file(path)

        result = await self._repo.get_users(
            self.handle_fields(fields), where_name, None, count
        )

        with open("file.txt", "w") as f:
            f.write(self.handle_users_data(result))

    def handle_fields(self, fields):
        return [field.replace(" ", "") for field in fields.split(",")]

    def handle_users_data(self, users: List[dict]):
        result = "LIST OF USERS \n" + "-" * 150 + "\n"
        for user in users:
            user_data = f"user_id: {user.pop('_id')} \n"
            for key, value in user.items():
                user_data += f"{key}: {value} \n"
            user_data += "-" * 150 + "\n"
            result += user_data
        return result
