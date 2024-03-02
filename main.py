from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain.answer import answer_router
from domain.question import question_router

app = FastAPI()

origins = [
    #"http://127.0.0.1:5173",    # 또는
    "http://localhost:5173"
]

app.add_middleware(  # CORS 설정 예외주소
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(question_router.router)
app.include_router(answer_router.router)























# @app.get("/hello")
# def hello():
#     return {"message": "안녕하세요 파이보입니다."}
#
#
#
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#

# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}