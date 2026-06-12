import os
import requests
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)
if __name__ == "__main__":
    openai_api_key = os.getenv('OPENAI_API_KEY')
    user_prompt = "What is the capital of France?"
    user_message = {"role": "user", "content": user_prompt}

    openai = OpenAI()

    response = openai.chat.completions.create(model="gpt-4.1-mini", messages=[user_message])
    print(response.choices[0].message.content)

