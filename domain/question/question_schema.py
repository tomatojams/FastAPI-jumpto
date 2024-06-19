import datetime

from pydantic import BaseModel, field_validator
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

class QuestionCreate(BaseModel):
    subject: str
    content: str

    @field_validator('subject', 'content')
    def not_empty(cls, v): # cls는 클래스 자신을 의미 v는 검증할 값
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v