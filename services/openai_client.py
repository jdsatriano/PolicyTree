import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def get_openai_client():
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("OpenAI API key is missing. Please set it in the .env file.")
    
    base_url = "https://api.openai.com/v1/chat/completions"
    
    client = OpenAI(
        api_key=api_key,
        organization=os.getenv('OPENAI_ORG_ID'),
        project='proj_LruZHkupTmn5HZLXWU844ULV'
    )

    return client
