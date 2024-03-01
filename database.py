'''
 SQLAlchemy 엔진 생성
엔진은 SQLAlchemy가 데이터베이스와 상호 작용할 때 사용하는 중요한 객체로, 데이터베이스 연결을 담당
connect_args={"check_same_thread": False}는 SQLite 데이터베이스와의 연결 설정 중 하나로,
현재 스레드에서만 사용 가능하도록 설정
create_engine은 커넥션 풀을 생성 => 데이터베이스 접속하는 객체를 일정수만큼만들어
돌려쓰는 방식으로 세션접속에 소요되는 시간 단축, 데이터베이스에 동시접속수 제어
'''
#import contextlib
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./myapi.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 데이터베이스 세션을 생성하는 sessionmaker 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#autocommit=False -> commit을 해야 변경사항 저장. 잘못저장되어도 rollback으로 취소가능
# SQLAlchemy 모델을 정의할 때 사용되는 베이스 클래스
Base = declarative_base()

# 데이터베이스 세션을 제공하는 컨텍스트 매니저
# 컨텍스트 매니저는 with 구문을 사용하여 데이터베이스 세션을 생성하고 반환하는데 사용

#@contextlib.contextmanager
# 라우터에서 dependency injection을 사용하기 위해 contextmanager를 사용하지 않는다.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# 제너레이터에서는 차례대로 결과를 반환하고자 return 대신 yield 키워드를 사용한다.
# 프로젝트 루트에 저장
