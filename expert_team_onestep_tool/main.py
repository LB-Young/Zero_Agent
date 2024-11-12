import asyncio
from domain_expert_team.leader import Leader
from llm_client import client, model

async def main():
    with open(r"F:\Cmodels\Zero_Agent\expert_team_onestep_tool\job_describe.txt", "r", encoding="utf-8") as f:
        job_describe = f.read()
    leader = Leader(role_leader=job_describe, agents=None, client=client, model=model)
    # result = await leader.execute("我是高考生，现在想要选专业，但是不知道选什么专业。请你介绍一下金融、法律和计算机三个专业分别有什么优点和缺点。")
    # query = "我是高考生，现在想要选专业，但是不知道选什么专业。请你介绍一下金融、法律和计算机三个专业分别有什么优点和缺点。"
    # query = "炒股的时候什么时候买进比较好？"
    # query = "请帮我生成一段冒泡排序代码和一段归并排序代码，调用代码执行器运行生成的代码，基于测试结果对比一下两种排序算法的优劣。"
    query = "请帮我生成一段选择排序的代码，调用代码执行器运行生成的代码，基于结果分析一下选择排序的特点"
    async for item in leader.execute(qeury=query):
        print(item, end="", flush=True)

    # print(result)

if __name__ == "__main__":
    # TODO: Add a command line interface
    asyncio.run(main())
 
