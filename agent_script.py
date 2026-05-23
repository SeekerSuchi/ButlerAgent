import os
from openai import OpenAI
from dotenv import load_dotenv 

load_dotenv()

client = OpenAI(
    api_key = os.getenv("LLM_API_KEY"),
    base_url = os.getenv("LLM_BASE_URL")
)

msgs = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello, how are you?"}
]

response = client.chat.completions.create(
    model = "gemini-2.5-flash",
    messages=msgs
)

print(response.choices[0].message.content)