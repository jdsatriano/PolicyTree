from openai import OpenAI
import os

def get_openai_client():
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("OpenAI API key is missing. Please set it in the .env file or environment variable.")
    client = OpenAI(
        organization='org-Y0UVheFiL7cBBjHAEak7oMtQ',
        project='proj_LruZHkupTmn5HZLXWU844ULV',
        api_key=api_key
    )
    return client