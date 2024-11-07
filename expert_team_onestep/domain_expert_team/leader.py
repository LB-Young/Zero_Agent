import re

class Leader:
    def __init__(self, role_leader, agents, client, model):
        self.role = role_leader
        self.agents = agents
        self.llm_client = client
        self.model = model

    async def agent_run(self, agent_name, agent_job):

        pass

    async def execute(self, qeury):
        prompt = self.role.format(prompt=qeury).strip()
        messages = [{"role": "user", "content": prompt}]
        result = self.llm_client.chat.completions.create(
                model=self.model,  # 请填写您要调用的模型名称
                messages=messages,
            )
        result = result.choices[0].message.content
        print("agent_result:", result)