import re


class NumberedPromptExtractor:
    def __init__(self, content):
        # Join the list elements with line breaks
        self.content = "\n".join(content)
        self.prompts = []

    def extract_prompts(self):
        prompt_lines = self.content.split("\n")
        for line in prompt_lines:
            match = re.match(r"^\d+\.\s*(.*)$", line)
            if match:
                prompt = match.group(1).strip()
                self.prompts.append(prompt)

    def get_prompts(self):
        return self.prompts
