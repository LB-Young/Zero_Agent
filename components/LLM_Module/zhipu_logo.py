import requests
from zhipuai import ZhipuAI
from load_api_key import load_api_key
client = ZhipuAI(api_key=load_api_key("zhipu"))  # 请填写您自己的APIKey

for i in range(20):
    response = client.chat.completions.create(
        model="glm-4-plus",  # 请填写您要调用的模型名称
        messages=[
            {"role": "user", "content": "我要创建一个讲解agent的app，现在需要为这个app构建一个logo，基于“agent”单词，请给我一个logo的设计方案，logo要简单明了、并且有足够的创意性。"}
        ],
    )
    print(response.choices[0].message)
    fangan = response.choices[0].message.content
    with open(r"F:\Cmodels\Zero_Agent\components\logos\fangan.txt", "a", encoding='utf-8') as f:
        f.write(str(i))
        f.write("\n")
        f.write(fangan)
        f.write("\n")
    for j in range(3):
        prompt = f"""
        {fangan}

        这是我设计的一个logo方案，请为这个方案生成一个logo图片。
        """
        response = client.images.generations(
            model="cogview-3-plus", #填写需要调用的模型编码
            prompt=prompt,
        )

        pic_url = response.data[0].url
        print(pic_url)
        response = requests.get(pic_url)
        with open(rf"F:\Cmodels\Zero_Agent\components\logos\{i}-{j}.jpg", "wb") as f:
            f.write(response.content)