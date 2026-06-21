''' Example script to show how to use Hugging Face's LLaMA implementation '''

from huggingface_hub import login
from transformers import AutoTokenizer
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

    # # load the tokenizer for LLaMA
    pipe = pipeline("text-generation", model="meta-llama/Llama-3.1-8B")
    tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3.1-8B")
    text = "I am excited to show Tokenizers in action to my LLM engineers"
    tokens = tokenizer.encode(text)
    print(tokens)