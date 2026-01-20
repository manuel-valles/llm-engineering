"""
This script demonstrates how to use Ollama (a local LLM) instead of cloud-based APIs.
Ollama runs locally and doesn't require an API key.
"""

import os
from dotenv import load_dotenv
from scraper import fetch_website_contents
from openai import OpenAI

# Load environment variables
load_dotenv(override=True)

# No API key is needed for local Ollama instances
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")

# Check if environment variables are set
if not OLLAMA_BASE_URL:
    raise ValueError("OLLAMA_BASE_URL environment variable is not set")
if not OLLAMA_MODEL:
    raise ValueError("OLLAMA_MODEL environment variable is not set")

# Initialize the OpenAI client for Ollama
client = OpenAI(base_url=OLLAMA_BASE_URL, api_key="not-needed")

# 1. Create a message and a dictionary
message = "Hello, Ollama! This is my first ever message to you!"
messages = [{"role": "user", "content": message}]

# 2. Call the API
print("\n--- Testing basic API call ---")
try:
    response = client.chat.completions.create(model=OLLAMA_MODEL, messages=messages)
    print(response.choices[0].message.content)
except Exception as e:
    print(f"Error: {e}")
    print("Make sure Ollama is running and the model is installed!")
    print(f"Install a model with: ollama pull {OLLAMA_MODEL}")

# 3. Define our system prompt
system_prompt = """
You are a snarky assistant that analyzes the contents of a website,
and provides a short, snarky, humorous summary, ignoring text that might be navigation related.
Respond in markdown. Do not wrap the markdown in a code block - respond just with the markdown.
"""

# Define our user prompt
user_prompt_prefix = """
Here are the contents of a website.
Provide a short summary of this website.
If it includes news or announcements, then summarize these too.
"""

# 4. Build useful messages for the API using a function and the Scrapper utility
def messages_for(website):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_prefix + website}
    ]

# 5. Test with CNN
print("\n--- Testing website scraping and summarization ---")
cnn = fetch_website_contents("https://cnn.com/")
print(f"Fetched {len(cnn)} characters from CNN")
print(f"Messages structure: {len(messages_for(cnn))} messages")
print(f"\nPreview of CNN content (first 500 characters):")
print(cnn[:500] + "..." if len(cnn) > 500 else cnn)

# 6. Time to bring it all together
def summarize(url):
    """Summarize a website using Ollama."""
    website = fetch_website_contents(url)
    response = client.chat.completions.create(
        model=OLLAMA_MODEL,
        messages=messages_for(website)
    )
    return response.choices[0].message.content

# 7. Test summarization
if __name__ == "__main__":
    print("\n--- Summarizing CNN ---")
    try:
        summary = summarize("https://cnn.com/")
        print("\nSummary:")
        print(summary)
    except Exception as e:
        print(f"Error during summarization: {e}")
        print("Make sure Ollama is running and the model is installed!")

        
if __name__ == "__main__":
    print("\n--- Summarizing Other Website ---")
    try:
        summary = summarize("https://manuel-valles.com/")
        print("\nSummary:")
        print(summary)
    except Exception as e:
        print(f"Error during summarization: {e}")
        print("Make sure Ollama is running and the model is installed!")
