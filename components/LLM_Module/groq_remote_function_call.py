import os
from load_api_key import load_api_key
from groq import Groq

client = Groq(
    api_key=load_api_key("groq"),
)


tools = [
    {
        "type": "function",
        "function": {
            "name": "通用问答",
            "description": "除了其他工具可以解决的问题之外的通用问题的问答接口",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "问题内容",
                    }
                },
                "required": ["query"]
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "单位换算",
            "description": "用于将单位换算成国际标准单位",
            "parameters": {
                "type": "object",
                "properties": {
                    "number": {
                        "type": "string",
                        "description": "待换算的数字"
                    },
                },
                "required": ["number"]
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "税收计算工具",
            "description": "个人所得税计算工具",
            "parameters": {
                "type": "object",
                "properties": {
                    "salaries": {
                        "type": "string",
                        "description": "个人收入（元）"
                    },
                },
                "required": ["salaries"]
            },
        }
    },
]



chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "工资一万缴纳多少税收",        
            }
    ],
    model="llama3-8b-8192",
    tools=tools,
    tool_choice="auto"
)
breakpoint()
print(chat_completion)
