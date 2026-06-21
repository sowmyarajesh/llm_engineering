from huggingface_hub import login
from transformers import AutoTokenizer, AutoModelForCausalLM,TextStreamer, BitsAndBytesConfig
import torch
import gc
from transformers import pipeline

### set up module path to import from utility
import sys  
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utility.huggingFace_utils import loginToHuggingFace

if __name__ == "__main__":
    # login to Hugging Face
    if not loginToHuggingFace():
        print("Failed to log in to Hugging Face")
        exit(1)

    