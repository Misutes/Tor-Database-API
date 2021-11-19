from typing import List

from pydantic import BaseModel


class UpdatedEmails(BaseModel):
    emails: List[str]
    state: int
