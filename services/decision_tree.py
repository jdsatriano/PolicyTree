import json
import os
import aiohttp
import asyncio
from pathlib import Path
from services.text_extraction import extract_text_from_policy
from services.openai_client import get_openai_client

def load_prompt():
    prompt_file_path = Path("prompts/decision_tree_prompt.txt")
    with open(prompt_file_path, "r") as file:
        return file.read()

async def generate_and_rank_tree(session, text):
    prompt_template = load_prompt()
    prompt = prompt_template.format(text=text)

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
    print("Processing files and generating decision trees")
    async with aiohttp.ClientSession() as session:
        tasks = []
        for filename in os.listdir(directory_path):
            if filename.endswith(".pdf"):
                filepath = os.path.join(directory_path, filename)
                tasks.append(process_pdf(filepath, session))
        results = await asyncio.gather(*tasks)
        return results
