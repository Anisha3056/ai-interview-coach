from google import genai
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def evaluate_answer(question_data, user_answer):

    prompt = f"""
    You are an expert technical interviewer.

    Interview Question:
    {question_data["question"]}

    Expected Points:
    {question_data["expected_points"]}

    Candidate Answer:
    {user_answer}

    Evaluate the answer.

    Return ONLY valid JSON:

    {{
        "score": 0,
        "strengths": [],
        "missing_points": [],
        "feedback": ""
    }}

    Rules:
    - Score should be between 0 and 10.
    - Compare against expected points.
    - Mention what the candidate did well.
    - Mention what they missed.
    - Give constructive feedback.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    response_text = response.text

    response_text = response_text.replace("```json", "")
    response_text = response_text.replace("```", "")
    response_text = response_text.strip()

    return json.loads(response_text)