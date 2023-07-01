from dotenv import load_dotenv
import os
import openai
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_prompt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Generate atleast 15 astonishing mid-journey images from the following content:{prompt}",
        max_tokens=999,
        temperature=0.98,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    return response.choices[0].text.strip()
