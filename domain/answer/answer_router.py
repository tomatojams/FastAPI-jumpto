from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from domain.answer import answer_crud, answer_schema
from domain.question import question_crud

router = APIRouter(
    prefix="/api/answer",
)

@router.post("/create/{question_id}", status_code=status.HTTP_204_NO_CONTENT)
#status_code=status.HTTP_204_NO_CONTENT 리턴할 응답이 없을 경우에는 응답코드 204를 리턴한다.
#즉 응답이 없다는 것을 명시적으로 표현하기 위해 사용한다.
def answer_create(question_id: int,
            _answer_create: answer_schema.AnswerCreate,
            db: Session = Depends(get_db)):

    # create_answer
    question = question_crud.get_question(db, question_id = question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    answer_crud.create_answer(db, question= question, answer_create=_answer_create)