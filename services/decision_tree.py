import json
from services.openai_client import get_openai_client

def generate_and_rank_tree(text):
    print("extracting and ranking tree")
    prompt = f"""
    Create a JSON decision tree to determine the medical necessity of the procedure 
    described in the provided text. The JSON should include: (1) "procedure_name" with 
    the name of the procedure; (2) "decision_tree" with questions, options, and decisions 
    covering initial approval and non-approval criteria; and (3) "quality" with a "ranking" 
    field as "High", "Moderate", or "Low", and an "explanation" field describing the ranking 
    based on completeness and integration. The tree should handle initial approval and non-approval. 
    Return only the JSON object, no extra text or code block markers.

    Format:
    "procedure_name": "Procedure name",
    "decision_tree":
        "question": "Initial question",
        "options":
            "yes":
                "question": "Next question",
                "options":
                    "yes":
                        "decision": "Approval"
                    "no":
                        "decision": "Non-approval"
            "no":
                "decision": "Non-approval"
    "quality":
        "ranking": "High",
        "explanation": "Reason for ranking"

    Below is the medical policy text:
    {text}
    """

    client = get_openai_client()
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert in natural language processing and medical data structuring."},
            {"role": "user", "content": prompt}
        ]
    )
    print("extracting and ranking tree: done")
    return json.loads(completion.choices[0].message.content)
