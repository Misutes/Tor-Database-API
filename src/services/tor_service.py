import os

import inject

from repositories.sqlite_repository import TorRepository
from utils.util import remove_file

service = None


@inject.autoparams()
def get_service(
    repo: TorRepository
):
    global service
    if service is None:
        service = TorService(repo)
    return service


class TorService:

    @inject.autoparams()
    def __init__(self, repo: TorRepository):
        self._repo = repo

    async def get_user(self, state, count):
        if result := [{"email": user.email, "state": user.state} for user in self._repo.get_users(state, count)]:
            return result
        return self._repo.count_users()

    async def update_users(self, emails, state):
        return self._repo.update_users(emails, state)

    async def get_register(self, count):
        if result := self._repo.get_register(count):
            processed, _ = await self._processed_register_email(result)
            return processed
        raise ValueError

    async def _processed_register_email(self, users):
        processed = []
        emails = []
        for user in users:
            emails.append(user.email)
            processed.append({"email": user.email, "state": user.state})
        self._repo.update_state(emails)
        return processed, emails

    async def get_file(self, path, count, service_number):
        remove_file(path)

        result = self._repo.get_register(count, service_number)
        _, emails = await self._processed_register_email(result)
        with open("file.txt", 'w') as f:
            f.write(
                '\n'.join(emails)
            )

