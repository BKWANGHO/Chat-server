import os
from fastapi import APIRouter
from pydantic import BaseModel
from app.api.titanic.service.titanic_service import TitanicService

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


router = APIRouter()

class Request(BaseModel):
    question: str

class Response(BaseModel):
    answer: str

service = TitanicService()

@router.post("/titanic")
async def titanic(req:Request):
   
    hello = 'C:\\Users\\bitcamp\\turingTeam\\chat-server\\backend\\app\\api\\context\\data\\hello.txt'
    
    f = open(hello, "r", encoding="utf-8")
    data = f.read()
    print(data)
    f.close()

    service.preprocess()
    
    print(req)

    return {"answer" : "생존자는 100명이야 "}

