import re
import json
from domain_expert_team.code_execute import code_execute

class Leader:
    def __init__(self, role_leader, agents, client, model):
        self.role = role_leader
        self.agents = agents
        self.llm_client = client
        self.model = model
        self.tools = {"code_execute": code_execute}

    async def agent_run(self, agent_name, agent_job):
        pass

    async def tool_run(self, tool_message):
        function_name, function_params = tool_message.split(":", 1)
        function_params_json = json.loads(function_params)
        need_params = await self.tools[function_name](params_format=True)
        extract_params = {}
        for param in need_params:
            extract_params[param] = function_params_json[param]
        result = await self.tools[function_name](**extract_params)
        return result

    async def execute(self, qeury):
        prompt = self.role.replace("{prompt}", qeury).strip()
        messages = [{"role": "user", "content": prompt}]
        result = self.llm_client.chat.completions.create(
                model=self.model,  # 请填写您要调用的模型名称
                messages=messages,
                stream=True
            )
        all_answer = ""
        tool_messages = ""
        tool_Flag = False
        for chunk in result:
            all_answer += chunk.choices[0].delta.content
            if tool_Flag:
                tool_messages += chunk.choices[0].delta.content
                continue
            if ":" in chunk.choices[0].delta.content and "=>$" in all_answer:
                tool_Flag = True
                tool_messages += chunk.choices[0].delta.content
                yield ": "
                continue
            yield chunk.choices[0].delta.content
        if tool_Flag:
            tool_messages = all_answer.split("=>$")[-1]
            result = await self.tool_run(tool_message=tool_messages)
            for item in str(result+"\n"):
                yield item
            query = qeury + "\n" + "已经执行内容:" + all_answer + "\n" + "工具执行结果:" + result
            async for item in self.execute(qeury=query):
                yield item
        # result = result.choices[0].message.content
        # print("agent_result:", result)