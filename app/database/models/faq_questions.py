from peewee import *
from database.connect import db
import uuid
import datetime
from playhouse.postgres_ext import *


class BaseModel(Model):
    class Meta:
        database = db


class FaqQuestions(BaseModel):
    id = UUIDField(primary_key=True, default=uuid.uuid4, index=True)
    question_abstract = CharField()
    
    class Meta:
        table_name = "faq_questions"