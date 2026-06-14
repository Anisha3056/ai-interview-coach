from pydantic import BaseModel
from typing import Dict, List


class QuestionRequest(BaseModel):
    analysis: Dict
    role: str
    interview_type: str
    previous_questions: List[Dict] 


class EvaluationRequest(BaseModel):
    question_data: Dict
    user_answer: str