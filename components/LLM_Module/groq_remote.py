import os
from load_api_key import load_api_key
from groq import Groq

client = Groq(
    api_key=load_api_key("groq")
)


chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)