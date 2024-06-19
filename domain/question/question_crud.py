from datetime import datetime
from domain.question.question_schema import QuestionCreate

from models import Question
from sqlalchemy.orm import Session

def get_question_list(db: Session):
    question_list = db.query(Question) \
.order_by(Question.create_date.desc()) \
        .all()
    return question_list

def get_question(db: Session, question_id: int):
    question = db.query(Question).get(question_id)
    return question

def create_question(db: Session, question_create: QuestionCreate):
    db_question = Question(subject= question_create.subject,
                           content= question_create.content,
                           create_date= datetime.now())
    db.add(db_question)
    db.commit()

'''
라우터에 위와 같이 데이터를 조회하는 부분을 포함해도 문제는 없다. 
하지만 파이보 프로젝트는 데이터를 처리하는 부분을 quesiton_crud.py 파일에 분리하여 작성하겠다.
왜냐하면 서로 다른 라우터에서 데이터를 처리하는 부분이 동일하여 중복될수 있기 때문이다.
'''