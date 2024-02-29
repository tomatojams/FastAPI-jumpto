import datetime

from pydantic import BaseModel


class Question(BaseModel):
    id: int
    subject: str
    content: str
    create_date: datetime.datetime
# subject: str | None = None # str 또는 None으로 타입을 지정 디펄트는 None

