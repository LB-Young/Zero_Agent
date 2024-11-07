from openai import OpenAI
from load_api_key import load_api_key
def send_messages(messages):
    response = client.chat.completions.create(
        model="deepseek-coder",
        messages=messages,
        tools=tools
    )
    
    #print(response)
    return response.choices[0].message


client = OpenAI(
    api_key=load_api_key("deepseek"),
    base_url="https://api.deepseek.com",
)

tools = [
    {
        "type": "function",
        "function": {
            "name": "search_file",
            "description": "查找文件",
            "parameters": {
                "type": "object",
                "properties": {
                    "tag": {
                        "type": "string",
                        "description": "文件的标签，比如行业，产品等，多个标签用/分割",
                    },
                    "time": {
                        "type": "string",
                        "description": "文件的时间，比如一周内，一天内，三天内，半个月内，一个月内等",
                    },
                    "writer": {
                        "type": "string",
                        "description": "文件的作者，一个具体的人名，比如某某某",
                    },
                    "content": {
                        "type": "string",
                        "description": "文件的内容描述",
                    },
                    "type": {
                        "type": "string",
                        "description": "文件格式，比如pdf,word,excel,ppt,视频,音频，图片等",
                    }
                },
                "required": ["content"]
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "search_person",
            "description": "查找人员",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "人员名字",
                    },
                    "place": {
                        "type": "string",
                        "description": "地点,比如深圳，北京，上海，杭州等",
                    },
                    "domain": {
                        "type": "string",
                        "description": "领域，比如互联网，金融，制造业等",
                    },
                    "team": {
                        "type": "string",
                        "description": "所在的部门或者团队，比如某某研发线，某部门，某团队等",
                    },
                    "position": {
                        "type": "string",
                        "description": "岗位，比如开发，测试，算法工程师等",
                    }
                },
                "required": []
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "answer_questions",
            "description": "回答问题",
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
            "name": "write_articles",
            "description": "写文章",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "文章标题"
                    },
                    "detail": {
                        "type": "string",
                        "description": "文章要求，侧重点或者风格"}
                },
                "required": ["query"]
            },
        }
    },
]
messages = [{"role": "user", "content": "请提供一个由哈宇豪撰写的关于领域认知智能的文件"}]
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=messages,
    tools=tools
)
#print(query)
breakpoint()
print(response.choices[0].message.tool_calls[0].function.arguments)