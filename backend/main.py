from fastapi import FastAPI
from langchain.chat_models.openai import ChatOpenAI
from langchain_openai import OpenAI
from dotenv import load_dotenv
from langchain.llms import OpenAI
import os
from langchain.schema import HumanMessage,AIMessage,SystemMessage
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
import uvicorn
from app.api.titanic.model.titanic_model import TitanicModel
from app.main_router import router



BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))


class Request(BaseModel):
    question: str

class Response(BaseModel):
    answer: str



app = FastAPI()

app.include_router(router,prefix= "/api")

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"hello": "world"}


@app.post("/chat")
def chatting(req:Request):
    print(req)

    chat= ChatOpenAI(
        openai_api_key=os.environ["api_key"],
        temperature=0.1,
        max_tokens=2048,
        model_name = 'gpt-3.5-turbo-0613'
    )
    # question = '대한민국의 수도는 뭐야?'질문Unexpected indentation

    # result = chat.predict(question)

    # print(f'[답변] : {result}')

    message= [
        SystemMessage(content="You are a traveler. I know the capitals of every country in the world",type="system"),
        HumanMessage(content="한국의 수도는 어디야 ?",type="human"),
        AIMessage(content="서울 입니다.", type="ai")
    ]

    print(f'[답변] : {chat.predict_messages(message)}')

    return  Response(answer=chat.predict(req.question))


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
