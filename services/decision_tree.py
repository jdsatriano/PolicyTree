import json
import os
import aiohttp
import asyncio
from services.text_extraction import extract_text_from_policy
from services.openai_client import get_openai_client

async def generate_and_rank_tree(session, text):
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
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are an expert in natural language processing and medical data structuring."},
            {"role": "user", "content": prompt}
        ]
    }

    async with session.post("https://api.openai.com/v1/chat/completions", json=payload, headers={"Authorization": f"Bearer {client.api_key}"}) as response:
        response = await response.json()
        return json.loads(response["choices"][0]["message"]["content"])

async def process_pdf(filepath, session):
    text = extract_text_from_policy(filepath)
    decision_tree = await generate_and_rank_tree(session, text)
    return decision_tree

async def process_all_pdfs_concurrently(directory_path):
    print("Processing files")
    async with aiohttp.ClientSession() as session:
        tasks = []
        for filename in os.listdir(directory_path):
            if filename.endswith(".pdf"):
                filepath = os.path.join(directory_path, filename)
                tasks.append(process_pdf(filepath, session))
        results = await asyncio.gather(*tasks)
        return results
