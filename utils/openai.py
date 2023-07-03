from dotenv import load_dotenv
import os
import openai
import re

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_prompt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Generate at least 2 astonishing mid-journey images from the following content:{prompt}",
        max_tokens=500,  # Adjust the max_tokens value as needed
        temperature=0.98,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    return response.choices[0].text.strip()


def get_sentences(content):
    pattern = r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s'
    sentences = re.split(pattern, content)
    return sentences


def generate_sentences_prompts(content):
    sentences = get_sentences(content)
    prompts = [generate_prompt(sentence) for sentence in sentences]
    return prompts
