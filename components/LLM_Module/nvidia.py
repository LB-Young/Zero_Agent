from openai import OpenAI
from load_api_key import load_api_key

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = load_api_key("nvidia_api")
)

completion = client.chat.completions.create(
  model="meta/llama-3.3-70b-instruct",
  messages=[{"role":"user","content":"在windows系统中，完成paper_recommend.sh脚本的代码，实现在每天早晨八点执行目录下的paper_recommend.py脚本。并且告诉我怎么运行"}],
  temperature=0.2,
  top_p=0.7,
  max_tokens=1024,
  stream=True
)

for chunk in completion:
  if chunk.choices[0].delta.content is not None:
    print(chunk.choices[0].delta.content, end="")

