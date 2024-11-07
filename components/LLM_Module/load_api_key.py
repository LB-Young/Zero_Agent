import json

async def ado_load_api_key(platform):
    with open(r"C:\Users\86187\Desktop\api_key.json", "r", encoding="utf-8") as f:
        api_dict = json.load(f)
    # print(api_dict)
    return api_dict.get(platform, None)

def load_api_key(platform):
    with open(r"C:\Users\86187\Desktop\api_key.json", "r", encoding="utf-8") as f:
        api_dict = json.load(f)
    # print(api_dict)
    return api_dict.get(platform, None)

if __name__ == "__main__":
    import asyncio
    print(asyncio.run(load_api_key("deepseek")))