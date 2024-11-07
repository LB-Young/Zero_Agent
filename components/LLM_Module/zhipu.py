import requests
from zhipuai import ZhipuAI
from load_api_key import load_api_key
client = ZhipuAI(api_key=load_api_key("zhipu"))  # 请填写您自己的APIKey


response = client.chat.completions.create(
    model="glm-4",  # 请填写您要调用的模型名称
    messages=[
        {"role": "user", "content": "写一首关于上海的诗，体现一下上海的繁华。"}
    ],
)
print(response.choices[0].message)
poetry = response.choices[0].message.content

prompt = f"""
{poetry}


请为这首诗配一副图，并且把这首诗写在图的右上角的区域，书写顺序为从上到下，从右向左。
"""
response = client.images.generations(
    model="cogview-3-plus", #填写需要调用的模型编码
    prompt=prompt,
)

pic_url = response.data[0].url
print(pic_url)
response = requests.get(pic_url)
with open("上海.jpg", "wb") as f:
    f.write(response.content)

prompt = f"""
{poetry}


请为这首诗配一个视频。
"""
response = client.videos.generations(
    model="cogvideox",
    prompt=prompt
)
print(response)
tatsk_id = response.id
while True:
    response = client.videos.retrieve_videos_result(
        id=tatsk_id
    )
    if response.task_status != "SUCCESS":
        import time
        time.sleep(1)
        continue
    video_url = response.video_result[0].url
    break

url = video_url

def download_video(url, filename):
    """
    下载视频并保存到本地文件。
    :param url: 视频的URL
    :param filename: 存储视频的本地文件名
    """
    # 发送HTTP GET请求获取视频内容
    response = requests.get(url, stream=True)
    
    # 检查请求是否成功
    if response.status_code == 200:
        # 打开一个本地文件用于写入
        with open(filename, 'wb') as f:
            # 迭代网络响应的二进制数据块
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print("视频下载完成")
    else:
        print("错误：无法从该URL下载视频")
download_video(url, '上海.mp4')