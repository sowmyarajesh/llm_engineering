# llm_engineering
Practice code for learning llm engineering


# Pre-requisite:

**.env:**

Get api key from the openAI. you may have to create account if you do not have one. 

create an .env file in the root path and provide the following details in the the .env file.

```
OPENAI_API_KEY=<API_KEY>
OPEN_AI_MODEL=<MODEL_NAME>
```

**ollama:**

Ollama can be useful to download and the models locally in the system so that not api calls will be needed.To try scripts related to ollama, it has to be installed and be running locally. 

Refer to instruction in  https://ollama.com/download

download the model *llama3.2* using the command ```ollama pull llama3.2```