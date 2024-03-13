import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPEN_API_KEY")
chat_completion = openai.chat.completions.create(
    messages=[
        {"role": "user", "content": "You are a puppy called Bummer."},
        {"role": "assistant", "content": "Woof!"},
        {"role": "user", "content": "What's your name?"},
    ],
    model="gpt-4",
)

print(chat_completion.choices[0].message.content)
