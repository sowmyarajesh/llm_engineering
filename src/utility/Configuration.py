import os
from dotenv import load_dotenv


def validateApiKey(api_key):
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
    api_key = validateApiKey(api_key)
    if api_key is None:
        return None
    config['api_key'] = api_key
    config['model'] = os.getenv('OPENAI_MODEL') if os.getenv('OPENAI_MODEL') is not None else "gpt-4.1-nano"
    return config