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