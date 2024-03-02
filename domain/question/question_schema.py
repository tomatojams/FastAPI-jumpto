import datetime

from pydantic import BaseModel
from domain.answer.answer_schema import Answer
'''
입출력 항목의 갯수와 타입을 설정
입출력 항목의 필수값 체크
입출력 항목의 데이터 검증
'''

#  Question 모델에 대한 스키마를 정의
# 스키마는 데이터의 구조, 유효성 검사 틀리면 에러를 발생시킴
class Question(BaseModel):
    id: int
    subject: str
    content: str
    create_date: datetime.datetime
    answer_list: list[Answer] = []
    # class Config:
    #     orm_mode = True