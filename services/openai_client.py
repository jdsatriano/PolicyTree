import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def get_openai_client():
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("OpenAI API key is missing")

    organization_id = os.getenv("OPENAI_ORG_ID")
    if not organization_id:
        raise ValueError("OpenAI Organization ID is missing")

    project_id = os.getenv("OPENAI_PROJECT_ID")
    if not project_id:
        raise ValueError("OpenAI Project ID is missing")
    
    base_url = "https://api.openai.com/v1/chat/completions"
    
    client = OpenAI(
        api_key=api_key,
        organization=organization_id,
        project=project_id
    )

    return client
