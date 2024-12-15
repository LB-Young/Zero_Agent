from volcenginesdkarkruntime import Ark
import os

from load_api_key import load_api_key
api_key = load_api_key("huoshan")
os.environ["ARK_API_KEY"] = api_key

client = Ark(
    base_url="https://ark.cn-beijing.volces.com/api/v3",
)

# Non-streaming:
print("----- standard request -----")
completion = client.chat.completions.create(
    model="ep-20241213094718-cpvqz",
    messages = [
        {"role": "user", "content": "常见的十字花科植物有哪些？"},
    ],
)
print(completion.choices[0].message.content)

# Streaming:
print("----- streaming request -----")
stream = client.chat.completions.create(
    model="ep-20241213094718-cpvqz",
    messages = [
        {"role": "user", "content": "常见的十字花科植物有哪些？"},
    ],
    stream=True
)
for chunk in stream:
    if not chunk.choices:
        continue
    print(chunk.choices[0].delta.content, end="")
print()