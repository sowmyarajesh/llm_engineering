""" Example script to chat completion api"""
import os
import requests
import sys
from pathlib import Path
ROOT = os.path.abspath("../")
sys.path.append(str(ROOT))

from utility.Configuration import getConfig

def make_api_call(config, messages):
    headers = {"Authorization": f"Bearer {config['api_key']}", "Content-Type": "application/json"}

    payload = {
        "model": config['model'],
        "messages": messages
        }
    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers=headers,
        json=payload
    )

    return response.json()["choices"][0]["message"]["content"]

def make_openai_call(config, messages):
    ## makes call using openai python library
    ## this makes the http call to the compatible api endpoint
    ## if you want to make call to specific api endpoint, key, you can pass it as argument to OpenAI(base_url=<API_URL>,api_key=<API_KEY>)
    from openai import OpenAI
    openai = OpenAI()

    response = openai.chat.completions.create(model=config['model'], messages=messages)
    return response.choices[0].message.content


if __name__ == "__main__":
    config = getConfig()
    messages = [{"role": "user", "content": "Tell me a fun fact"}]
    result1 = make_api_call(config, messages)
    print("result from api call thru request method:::")
    print(result1)
    result2 = make_openai_call(config, messages)
    result1 = make_api_call(config, messages)
    print("result from api call thru python library method:::")
    print(result2)