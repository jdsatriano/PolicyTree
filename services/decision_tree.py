import json
from services.openai_client import get_openai_client

def generate_and_rank_tree(text):
    print("extracting and ranking tree")
    prompt = f"""
    I have a medical policy document. Extract the medical guidelines and build a JSON decision tree that is clear and concise. Show clear paths for what is medically necessary and what is not. Follow these guidelines:

    1. Identify sections that outline medical necessity criteria and non-medical necessity criteria.
    2. Structure the decision tree:
    - Use section headings as top-level keys.
    - Include sub-criteria under each top-level key based on the document's structure.
    3. Logical selection criteria:
    - Specify whether all conditions ("all") must be met or if any one condition ("any") must be met.
    - Differentiate between "Medically Necessary" and "Not Medically Necessary" criteria.

    Please return only the JSON object, without any explanations or additional text. Do not wrap the JSON object in code block markers.

    Below is the medical policy text:
    {text}

    Here is an example of what the structure should be:

    Medical_Procedure:
    Medically_Necessary:
        Procedure_Type:
        Criteria:
            Indications:
                any: ["Condition A", "Condition B"]
            Treatment_Criteria:
                all: ["Treatment A", "Expected Outcome"]
            Clinical_Criteria:
                any: [
                "Clinical Condition A",
                "Clinical Condition B",
                "Clinical Condition C"
                ]
    Not_Medically_Necessary:
        - "Criteria for Procedure_Type not met"
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
