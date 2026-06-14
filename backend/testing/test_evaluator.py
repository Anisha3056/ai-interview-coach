from services.evaluator import evaluate_answer

question_data = {
    "question":
    "Why did you choose Sentence Transformers instead of TF-IDF?",

    "expected_points": [
        "Semantic understanding",
        "Context-aware embeddings",
        "Cosine similarity",
        "Comparison with TF-IDF",
        "Tradeoffs"
    ]
}

user_answer = """
I used Sentence Transformers because
they generate context-aware embeddings.

Unlike TF-IDF's bag-of-words approach, which uses key word frequency and matching, 
Sentence Transformers understand the meaning of words
based on surrounding context.

These embeddings were compared using
cosine similarity to compare user queries with Airbnb listings.

Though embeddings generation did improve the recommendation quality, the tradeoff 
was increased computational cost and storage requirements compared to TF-IDF.
"""

result = evaluate_answer(
    question_data,
    user_answer
)

print(result)