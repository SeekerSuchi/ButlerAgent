import os
from openai import OpenAI
from dotenv import load_dotenv 

load_dotenv()

client = OpenAI(
    api_key = os.getenv("LLM_API_KEY"),
    base_url = os.getenv("LLM_BASE_URL")
)

system_prompt = """You are a Personal Assistant named SeekieSen capable of reasoning and using tools.
For each user request:
1. Analyze what needs to be done
2. Determine which tools (if any) are needed
3. Use tools to gather information or take actions
4. Evaluate the results
5. Continue until the goal is achieved
"""

msgs = [
    {"role": "system", "content": system_prompt},
]

def ask_seekie(user_query, conversation_history=msgs, client=client):
    conversation_history.append({"role" : "user", "content" : user_query})
    response = client.chat.completions.create(
        model = "gemini-2.5-flash",
        messages=conversation_history
    )
    conversation_history.append({"role" : "assistant", "content" : response.choices[0].message.content})
    
    return response

def chat_loop():
    print("SeekieSen started!\n")
    print("Type 'exit' to quit\n")
    user_query = input("You: ")
    while user_query != "exit":
        response = ask_seekie(user_query, msgs, client)
        print("Seekie: ", response.choices[0].message.content , "\n")
        user_query = input("You: ")

chat_loop()