import asyncio
from domain_expert_team.leader import Leader
from llm_client import client, model

async def main():
    with open(r"F:\Cmodels\Zero_Agent\roleplay_onestep\job_describe.txt", "r", encoding="utf-8") as f:
        job_describe = f.read()
    leader = Leader(role_leader=job_describe, agents=None, client=client, model=model)
    with open(r"C:\Users\86187\Desktop\test.txt", "r", encoding="utf-8") as f:
        reference = f.read()
    query = f"请根据以下参考信息回答问题：\n{reference}\n\n问题：介绍一下这篇文章的内容"
    # result = await leader.execute("我是高考生，现在想要选专业，但是不知道选什么专业。请你介绍一下金融、法律和计算机三个专业分别有什么优点和缺点。")
    async for item in leader.execute(qeury=query):
        print(item, end="", flush=True)

    # print(result)

if __name__ == "__main__":
    # TODO: Add a command line interface
    asyncio.run(main())