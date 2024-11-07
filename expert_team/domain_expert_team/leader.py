import re
from .expert import Expert

class Leader:
    def __init__(self, role_leader, agents, client, model):
        self.role = role_leader
        self.agents = agents
        self.llm_client = client
        self.model = model

    async def agent_run(self, agent_name, agent_job):

        pass

    async def execute(self, qeury):
        all_result = ""
        finished_flag = "start"
        finished_steps = []
        times = 0
        while finished_flag != "None" and times < 10:
            times += 1
            if len(finished_steps) == 0:
                result_format = "当前问题还未完成任何步骤！"
            else:
                result_format = " - ".join(finished_steps)
            prompt = self.role.format(prompt=qeury, finished_steps=result_format).strip()
            messages = [{"role": "user", "content": prompt}]
            result = self.llm_client.chat.completions.create(
                    model=self.model,  # 请填写您要调用的模型名称
                    messages=messages,
                )
            result = result.choices[0].message.content
            print("agent_result:", result)
            match = re.search(r"=>@(.+?):(.+)", result)
            if match:
                agent_name = match.group(1)
                agent_job = match.group(2)
                if agent_name != "None":
                    if agent_name in self.agents.keys():
                        agent_obj = self.agents[agent_name]
                        result = await agent_obj.execute(agent_job)
                        print("agent_result:", result)
                        all_result += result + "\n\n"
                        finished_steps.append(f"{agent_name}已经完成了{agent_job},结果为{result}")
                        finished_flag = agent_name
                    else:
                        result = self.llm_client.chat.completions.create(
                                            model=self.model,  # 请填写您要调用的模型名称
                                            messages=[{'role':'user', 'content':agent_job}],
                                        )
                        result = result.choices[0].message.content
                        print("agent_result:", result)
                        all_result += result + "\n\n"
                        finished_steps.append(f"{agent_name}已经完成了{agent_job},结果为{result}")
                        finished_flag = agent_name
                else:
                    finished_flag = "None"
            else:
                continue
        return all_result