import os
from together import Together
from load_api_key import load_api_key
client = Together(api_key=load_api_key("together"))

response = client.chat.completions.create(
    model="meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
    messages=[
        {
            "role": "user",
            "content": "hello",
        }
    ],
    max_tokens=1000,
    temperature=0.7,
    top_p=0.7,
    top_k=50,
    repetition_penalty=1,
    stop=["<|eot_id|>"],
    stream=False
)
print(response.choices[0].message.content)