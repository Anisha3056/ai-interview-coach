from pydantic import BaseModel


class InterviewSessionRequest(BaseModel):

    user_id: int

    role: str

    interview_type: str

    score: int