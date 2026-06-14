from google import genai
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_question(
    analysis,
    role,
    interview_type,
    previous_questions
):
    previous_questions_text = ""

    for item in previous_questions:
        previous_questions_text += f"""
Question: {item.get('question', '')}
Topic: {item.get('topic', '')}
Interview Type: {item.get('interview_type', '')}

"""

    prompt = f"""
You are a Senior Technical Interviewer at a top technology company.

Candidate Resume Analysis:
{analysis}

Target Role:
{role}

Interview Type:
{interview_type}

Previously Asked Questions:
{previous_questions_text}

==================================================
QUESTION GENERATION RULES
==================================================

1. Generate ONLY ONE interview question.

IMPORTANT:

Avoid repeating:

* Previously asked questions

* Previously covered topics

* Previously covered interview types

If a previous question was:

Topic: Class Imbalance

Do NOT generate another question about:

- SMOTE
- ADASYN
- Class Weights
- Imbalanced Data

Choose an entirely different area.

If previous interview type was:

Project Based

Prefer another project,
technology,
skill,
or concept.

Ensure variety throughout the interview.

2. The question should be realistic and similar
   to questions asked in actual interviews.

3. Difficulty should be:
   Easy, Medium, or Hard.

4. The question should encourage deep thinking,
   not simple yes/no answers.
   


==================================================
INTERVIEW TYPE INSTRUCTIONS
==================================================

IF interview_type = "Project Based":

- Focus on projects mentioned in the resume.
- Ask about:
    - architecture
    - design decisions
    - trade-offs
    - model selection
    - evaluation metrics
    - deployment
    - scalability
    - limitations
    - future improvements

Examples:
- Why did you choose XGBoost?
- Why did you use SMOTE?
- How would you scale this system?
- What challenges did you face?

--------------------------------------------------

IF interview_type = "Behavioral":

Generate a behavioral interview question.

Focus on:
- teamwork
- leadership
- conflict resolution
- communication
- ownership
- problem solving
- failure
- learning from mistakes
- handling pressure
- time management

Examples:
- Tell me about a challenge.
- Tell me about a disagreement in a team.
- Describe a difficult deadline.
- Tell me about a failure.

--------------------------------------------------

IF interview_type = "Tech Stack":

Generate a question based on technologies
mentioned in the resume.

Focus on:
- Python
- FastAPI
- React
- Docker
- Pandas
- NumPy
- MLflow
- SQL
- MongoDB
- Machine Learning libraries
- APIs
- Git

Ask implementation-level questions.

--------------------------------------------------

IF interview_type = "System Design":

Generate a system design question relevant
to the target role.

Examples:

For Data Science:
- Design a recommendation system
- Design a fraud detection system
- Design a churn prediction platform

For ML Roles:
- Design an MLOps pipeline
- Design a model monitoring system
- Design a real-time prediction service

Focus on:
- scalability
- architecture
- trade-offs
- databases
- deployment

--------------------------------------------------

IF interview_type = "Machine Learning Fundamentals":

Generate a conceptual ML question.

Topics may include:

- Bias vs Variance
- Supervised vs Unsupervised Learning
- Regression vs Classification
- Precision
- Recall
- F1 Score
- ROC-AUC
- Cross Validation
- Feature Engineering
- Class Imbalance
- XGBoost
- Random Forest
- Regularization
- Overfitting
- Ensemble Learning
- Model Evaluation

The question should test understanding,
not memorization.

--------------------------------------------------

IF interview_type = "DSA":

Generate an entry-level or intermediate
DSA interview question.

Topics:

- Arrays
- Strings
- Hash Maps
- Sliding Window
- Sorting
- Binary Search
- Linked Lists
- Trees
- Graphs
- Recursion

Avoid extremely difficult competitive
programming problems.

==================================================
OUTPUT FORMAT
==================================================

Return ONLY valid JSON.

{{
    "question": "generated question",
    "difficulty": "Easy/Medium/Hard",
    "topic": "main topic",
    "expected_points": [
        "point1",
        "point2",
        "point3"
    ],
    "follow_up_question": "one relevant follow-up question"
}}
"""

    try:
        response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
    except Exception:
        return {"error":"Gemini quota exceeded. Please try again later."}

    response_text = response.text

    response_text = response_text.replace("```json", "")
    response_text = response_text.replace("```", "")
    response_text = response_text.strip()

    return json.loads(response_text)