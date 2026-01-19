# Beyond OpenAI

The companies behind LLMs, such as OpenAI and Google (Gemini), have built web endpoints. You call their models by making an HTTP request to a Web Address and passing in all the information about your prompts.

To make this simple, the team at OpenAI wrote a python utility known as a _Python Client Library_ which wraps the HTTP call. So you write python code and it calls the web. And THAT is what the library `openai` is.

It is:
- A lightweight python utility
- Turns your python requests into an HTTP call
- Converts the results coming back from the HTTP call into python objects

## Use of the library `openai`:

```python
# Create an OpenAI python client for making web calls to OpenAI
openai = OpenAI()

# Make the call to https://api.openai.com/v1/chat/completions
response = openai.chat.completions.create(model="gpt-4.1-mini", messages=[{"role":"user", "content": "what is 2+2?"}])

# Print the result
print(response.choices[0].message.content)
```

The API documentation for:
- [Direct web HTTP calls](https://platform.openai.com/docs/guides/text?api-mode=chat&lang=curl)  
- [Python Client Library](https://platform.openai.com/docs/guides/text?api-mode=chat&lang=python)

## Use other LLMs

All the other major LLMs have API endpoints that are compatible with OpenAI. You can use the utility for converting python to web requests. Openai allows you to change the utility from calling `https://api.openai/com/v1` to calling any web address that you specify.

And so you can use the OpenAI utility even for calling models that are NOT OpenAI, like this:

`not_actually_openai = OpenAI(base_url="https://somewhere.completely.different/", api_key="another_providers_key")`

Here are all the OpenAI-compatible endpoints from the major providers. It even includes using Ollama, locally. Ollama provides an endpoint on your local machine, and they made it OpenAI compatible too - very convenient.

```python
ANTHROPIC_BASE_URL = "https://api.anthropic.com/v1/"
DEEPSEEK_BASE_URL = "https://api.deepseek.com/v1"
GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
GROK_BASE_URL = "https://api.x.ai/v1"
GROQ_BASE_URL = "https://api.groq.com/openai/v1"
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
OLLAMA_BASE_URL = "http://localhost:11434/v1"
```

### Using Gemini (FREE - Not even account needed!)

1. Visit Google Studio to set up an account: https://aistudio.google.com/  
2. Add your key as _GOOGLE_API_KEY_ and _GEMINI_API_KEY_ to your `.env`  

Then:

```python
import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv(override=True)

GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
google_api_key = os.getenv("GOOGLE_API_KEY")
gemini = OpenAI(base_url=GEMINI_BASE_URL, api_key=google_api_key)
response = gemini.chat.completions.create(model="gemini-2.5-flash-preview-05-20", messages=[{"role":"user", "content": "what is 2+2?"}])
print(response.choices[0].message.content)
```