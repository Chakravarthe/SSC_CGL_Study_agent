""" Request and response DTOs for the API """
from datetime import date
from typing import List, Optional
from pydantic import BaseModel, Field

class StudentCreate(BaseModel):
    name: str = Field(min_length = 1, max_length = 100)
    email_date: date
    hours_per_day: float = Field(default = 2.0, gt=0, le=16)

class TopicStatus(BaseModel):
    topic: str
    mastery: float
    next_review: Optional[date]

class StudentStatus(BaseModel):
    id: int
    name: str
    days_left: int
    phase: str
    streak: int
    topics: List[TopicStatus]

class QuestionOut(BaseModel):
    id: int
    topic: str
    text: str
    difficult: int
    real_life_hint: str

class AnswerIn(BaseModel):
    answer: float

class AnswerResult(BaseModel):
    correct: bool
    correct_answer: float
    explanation: str
    mastery: float
    next_review: Optional[date]

class DailyPlan(BaseModel):
    days_left: int
    phase: str
    review_topics: List[TopicStatus]
    focus_topic: Optional[str]
    topics: List[TopicStatus]