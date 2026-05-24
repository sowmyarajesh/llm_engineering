"""
This script needs ollama installed and running locally in the system.
This example to see if we can run the model locally without any api calls. 

"""
from openai import OpenAI
OLLAMA_BASE_URL = "http://localhost:11434/v1"
OLLAMA_MODEL ="llama3.2:latest"

if __name__=="__main__":
    
    messages = [{"role": "user", "content": "Tell me a fun fact"}]
    ollama = OpenAI(base_url=OLLAMA_BASE_URL, api_key='ollama')
    response = ollama.chat.completions.create(model=OLLAMA_MODEL, messages=[{"role": "user", "content": "Tell me a fun fact"}])
    print(response.choices[0].message.content)