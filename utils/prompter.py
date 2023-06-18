from typing import Any
from utils.openai import generate_prompt


class Prompter:
    def __init__(self, content):
        self.content = content
        self.prompts = []

    def generate_prompts(self):
        prompts = generate_prompt(self.content)
        prompts_array = [prompt.strip()
                         for prompt in prompts.split('\n') if prompt.strip()]
        for i, prompt in enumerate(prompts_array, start=1):
            self.prompts.append(prompt)

    def get_prompts(self):
        return self.prompts
