import dataclasses
from server.database import requests
import json

class User:
    def __init__(self, user_id: int):
        self.__dict__ = json.loads(requests.DbOperator().select_user_info(user_id))

@dataclasses.dataclass
class Task:
    title: str
    text: str
    is_secret: bool
    task_id: int
    from_id: int
    to_id: int
    progress_start: int
    progress_end: int