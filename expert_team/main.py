import asyncio
from domain_expert_team.expert import Expert
from domain_expert_team.leader import Leader
from llm_client import client, model

async def main():
    with open(r"F:\Cmodels\Zero_Agent\agent-team\job_describe.txt", "r", encoding="utf-8") as f:
        job_describe = f.read()
    agent_prompt_list = job_describe.split("---------------------------------------------------------")
    agents = {}
    for agent_prompt in agent_prompt_list[:-1]:
        agent_name = agent_prompt.split("- name: ")[-1].split("\n")[0].strip()
        agent_obj = Expert(agent_prompt, client, model)
        agents[agent_name] = agent_obj
    leader = Leader(agent_prompt_list[-1], agents, client, model)
    result = await leader.execute("我是高考生，现在想要选专业，但是不知道选什么专业。请你介绍一下金融、法律和计算机三个专业分别有什么优点和缺点。")
    # result = await leader.execute(qeury="炒股的时候什么时候买进比较好？")
    # print(result)

if __name__ == "__main__":
    # TODO: Add a command line interface
    asyncio.run(main())