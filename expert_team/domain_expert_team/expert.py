


class Expert:
    def __init__(self, role_prompt, client, model):
        self.role_prompt = role_prompt
        self.client = client
        self.model = model

    async def execute(self, prompt):
        # TODO: Implement the designer role
        prompt = self.role_prompt.format(prompt=prompt)
        result = self.client.chat.completions.create(
                    model=self.model,  # 请填写您要调用的模型名称
                    messages=[
                        {"role": "user", "content": prompt}
                    ],
                )
        return result.choices[0].message.content