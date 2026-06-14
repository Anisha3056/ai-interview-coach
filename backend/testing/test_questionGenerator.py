from services.question_generator import generate_question

analysis = {
    "candidate_name": "TENALI ANISHA",
    "skills": [
        "Python",
        "FastAPI",
        "React",
        "Sentence Transformers"
    ],
    "projects": [
        {
            "title":
            "AI Travel Companion – Airbnb Recommendation System"
        }
    ]
}

result = generate_question(
    analysis,
    "Machine Learning Engineer"
)

print(result)