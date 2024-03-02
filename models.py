from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
'''
Base는 database.py에서 정의한 Base 클래스를 가져옴
'''

class Question(Base):
    __tablename__ = "question"
    id = Column(Integer, primary_key=True)
    # primary_key는 자동으로 1씩 증가
    subject = Column(String, nullable=False)
    # nullable=False는 빈값을 허용하지 않음
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)

class Answer(Base):
    __tablename__ = "answer"

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    question_id = Column(Integer, ForeignKey("question.id"))
    question = relationship("Question", backref="answer_list")
    # 마지막줄은 칼럼이 아니라 관계를 나타내므로 Column이 아닌 relationship을 사용
    # question을 바꾸면 글이 올라가지 않음 체크포인트


    # Question 관게설정하는 클래스 지정, Question 객체에서 Answer 객체에 접근할 때 사용
    #  따라서 Question 인스턴스가 있으면 answers 속성을 통해 답변을 억세스 가능, 반대도 가능
    # answer.question.subject 처럼 마치 객체의 속성처럼 접근가능. question.answer.content도 가능