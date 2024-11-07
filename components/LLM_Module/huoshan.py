"""
pip install 'volcengine-python-sdk[ark]'

import os
from volcenginesdkarkruntime import Ark

client = Ark(
    api_key=os.environ.get("ARK_API_KEY")
    timeout=120
    max_retries=2
)
"""
import os
from volcenginesdkarkruntime import Ark

client = Ark(
    api_key="",
    timeout=120,
    max_retries=2
)

response = client.chat.completions.create(
    model="Doubao-pro-4k",  # 请填写您要调用的模型名称
    messages=[
        {"role": "user", "content": "作为一名营销专家，请为我的产品创作一个吸引人的口号"},
        {"role": "assistant", "content": "当然，要创作一个吸引人的口号，请告诉我一些关于您产品的信息"},
        {"role": "user", "content": "智谱AI开放平台"},
        {"role": "assistant", "content": "点燃未来，智谱AI绘制无限，让创新触手可及！"},
        {"role": "user", "content": "创作一个更精准且吸引人的口号"}
    ],
)
print(response.choices[0].message)