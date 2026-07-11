from google import genai
import time
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def analyze_resume(resume_text):

    prompt =  f"""
    Analyze this resume.
    
    Resume: {resume_text}

    Return ONLY valid JSON.

    {{
        "candidate_name": "",
        "skills": [],
        "projects": [],
        "strengths": [],
        "experience": [],
        "recommended_roles": []
    }}
    """
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            break
        except Exception as e:
            if attempt < 2:
                time.sleep(2)
            else:
                raise

    response_text = response.text
    response_text = response_text.replace("```json", "")
    response_text = response_text.replace("```", "")
    response_text = response_text.strip()
    data = json.loads(response_text)
    return data