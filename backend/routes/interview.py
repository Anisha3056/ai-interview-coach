from fastapi import APIRouter

from models.interview import (
    QuestionRequest,
    EvaluationRequest
)

from services.question_generator import (
    generate_question
)

from services.evaluator import (
    evaluate_answer
)

from database.db import SessionLocal

from models.interview_sessions import (
    InterviewSession
)

from models.interview_sessions_schema import (
    InterviewSessionRequest
)

from database.db import SessionLocal

from models.interview_sessions import (
    InterviewSession
)
router = APIRouter()

@router.post("/question")
async def create_question(
    request: QuestionRequest
):

    result = generate_question(
        request.analysis,
        request.role,
        request.interview_type,
        request.previous_questions
    )

    return result

@router.post("/evaluate")
async def evaluate(
    request: EvaluationRequest
):

    result = evaluate_answer(
        request.question_data,
        request.user_answer
    )

    return result

@router.post("/save")
def save_interview_session(
    request: InterviewSessionRequest
):

    db = SessionLocal()

    session = InterviewSession(

        user_id=request.user_id,

        role=request.role,

        interview_type=request.interview_type,

        score=request.score

    )

    db.add(session)

    db.commit()

    db.refresh(session)

    return {

        "message":
        "Interview saved successfully",

        "session_id":
        session.id

    }
    
@router.get("/history/{user_id}")
def get_interview_history(
    user_id: int
):

    db = SessionLocal()

    interviews = (
        db.query(
            InterviewSession
        )
        .filter(
            InterviewSession.user_id == user_id
        )
        .all()
    )

    return interviews

@router.get("/progress/{user_id}")
def get_progress(
    user_id: int
):

    db = SessionLocal()

    interviews = (
        db.query(
            InterviewSession
        )
        .filter(
            InterviewSession.user_id == user_id
        )
        .all()
    )

    if not interviews:

        return {
            "message":
            "No interviews found"
        }

    scores = [
        interview.score
        for interview in interviews
    ]

    return {

        "total_interviews":
            len(interviews),

        "average_score":
            round(
                sum(scores)
                /
                len(scores),
                2
            ),

        "best_score":
            max(scores),

        "latest_score":
            interviews[-1].score

    }