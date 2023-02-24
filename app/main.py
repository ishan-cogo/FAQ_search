from typing import Union
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from database.connect import db
from nlp.get_chatbot_response import get_chatbot_response

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup():
    if db.is_closed():
        db.connect()


@app.get("/")
def read_root():
    return {"Hello": "CogoBot"}


@app.get("/get_chatbot_response")
def get_chatbot_response_func(question: str):
    return get_chatbot_response(question)
    # return {"questions_faq_id":get_chatbot_response(question)}