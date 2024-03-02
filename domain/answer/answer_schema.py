from pydantic import BaseModel, field_validator

class AnswerCreate(BaseModel):
    content: str
    @field_validator('content')
    def not_empty(cls, v): # cls는 클래스 자신을 의미 v는 검증할 값
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v
