from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db

from database import SessionLocal
from models import Question

router = APIRouter(
    prefix="/api/question",
)
'''
"/api/question"으로 시작하는 URL을 가진 모든 경로에 대한 라우터 인스턴스를 생성
라우팅이란 FastAPI가 요청받은 URL을 해석하여 그에 맞는 함수를 실행하여 그 결과를 리턴하는 행위를 말한다.
'''

@router.get("/list")
#"/api/question/list"에 대한 HTTP GET 요청을 처리하기 위한 경로를 정의
def question_list(db: Session = Depends(get_db)):
    # db = SessionLocal()
    # #SessionLocal()을 사용하여 새 데이터베이스 세션을 생성
    # _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    # #Question 모델을 쿼리하고 결과를 create_date 속성을 기준으로 내림차순으로 정렬하여 질문 목록을 가져옵니다.
    # db.close()
    # #데이터베이스 세션 반환(O), 커넥션풀 반환(O)\ , 세션종료(X)가 아니다.
    # return _question_list

    # with 사용
    # with get_db() as db:
    #     _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    #     return _question_list

    # Dependency Injection 사용
    _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    return _question_list
'''
FastAPI의 Depends는 매개 변수로 전달 받은 함수를 실행시킨 결과를 리턴한다. 
따라서 db: Session = Depends(get_db)의 db 객체에는 get_db 제너레이터에 의해 생성된 세션 객체가 주입된다. 
이 때 get_db 함수에 자동으로 contextmanager가 적용되기 때문에(Depends에서 contextmanager를 적용하게끔 설계되어 있다.) 
database.py의 get_db 함수는 다음과 같이 적용한 @contextlib.contextmanager 어노테이션을 제거해야 한다.
'''