"""Hugging Face Utilities"""
from huggingface_hub import login, whoami
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utility.Configuration import getConfig
CONFIG = getConfig()

def loginToHuggingFace():
    if CONFIG is None:
        print("Config is not set up correctly - please fix the issues identified in the troubleshooting notebook")
        return False
    hf_token = CONFIG.get("HF_TOKEN")
    if hf_token and hf_token.startswith("hf_"):
        print("HF key looks good so far")
        login(token=hf_token)
        # Verify the token is valid by fetching the current user
        user_info = whoami(token=hf_token)
        print(f"[SUCCESS] Logged in to Hugging Face as: {user_info.get('name', 'Unknown')}")
        return True
    else:
        print("HF key is not set - please click the key in the left sidebar")
        return False