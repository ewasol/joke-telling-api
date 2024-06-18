from src.joke_api.processing.text.generate_answer import generate_openai_answer


def create_text(topic: str) -> str:
    prompt = create_prompt(topic)
    response = generate_openai_answer(prompt)
    text = response.choices[0].message.content
    return text.strip()


def create_prompt(topic: str) -> str:
    topic = topic.strip()
    return f"Write a joke about {topic}."
