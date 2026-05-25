""" Introduction to LLM Engineering 

This module contains examples of how to use LLMs in a variety of ways.
"""

import os
from dotenv import load_dotenv
from IPython.display import Markdown, display
from openai import OpenAI

import sys
from pathlib import Path
ROOT = os.path.abspath("../src")
sys.path.append(str(ROOT))


def vallidateApiKey(api_key):
    if not api_key:
        print("No API key was found - please head over to the troubleshooting notebook in this folder to identify & fix!")
        return None
    elif not api_key.startswith("sk-proj-"):
        print("An API key was found, but it doesn't start sk-proj-; please check you're using the right key - see troubleshooting notebook")
        return None
    elif api_key.strip() != api_key:
        print("An API key was found, but it looks like it might have space or tab characters at the start or end - please remove them - see troubleshooting notebook")
        return None
    
    print("API key found and looks good so far!")
    return api_key

def getConfig():
    config = { }
    load_dotenv(override=True)
    api_key = os.getenv('OPENAI_API_KEY')
    api_key = vallidateApiKey(api_key)
    if api_key is None:
        return None
    config['api_key'] = api_key
    config['model'] = os.getenv('OPENAI_MODEL') if os.getenv('OPENAI_MODEL') is not None else "gpt-4.1-nano"
    return config

if __name__ == "__main__":
    config = getConfig()
    if config is None or config["api_key"] is None or config["model"] is None:
        print("Check the env file and try again")
    else:
        openai = OpenAI()
        # Step 1: define prompts
        system_prompt = "You are  junior ml engineer"
        user_prompt = """
            Here is the content of a literature publication. Provide a summary of the content in this website. 

        """
        _website = "https://www.mdpi.com/journal/aieng"

        # Step 2: Make the messages list
        messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt + _website}
            ]

        # Step 3: Call OpenAI
        response = openai.chat.completions.create(
                model = config["model"],
                messages = messages
            )
        result =  response.choices[0].message.content

        # Step 4: print the result
        print(result)
