import datetime

from pydantic import BaseModel
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
    # class Config:
    #     orm_mode = True
        # orm_mode는 Pydantic 모델이 SQLAlchemy 모델을 반환할 때 필요한 설정이다.
        # 이 설정을 추가하면 Pydantic 모델이 SQLAlchemy 모델을 반환할 때,
        # SQLAlchemy 모델의 컬럼을 그대로 반환하도록 설정한다.
# subject: str | None = None # str 또는 None으로 타입을 지정 디펄트는 None

