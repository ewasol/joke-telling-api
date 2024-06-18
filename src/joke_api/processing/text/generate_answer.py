from openai import OpenAI
from openai.types.chat import ChatCompletion

from src.joke_api.config import Config

openai_client = OpenAI(api_key=Config.OPENAI_KEY)


def generate_openai_answer(prompt: str) -> ChatCompletion:
    messages = [{"role": "user", "content": prompt}]
    response = openai_client.chat.completions.create(
        model=Config.MODEL,
        messages=messages,
        temperature=0,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    return response
