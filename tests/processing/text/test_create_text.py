from unittest.mock import MagicMock

import pytest
from mock import patch
from openai.types.chat import ChatCompletion

from src.joke_api.processing.text.create_text import create_text


@patch("src.joke_api.processing.text.create_text.generate_openai_answer")
def test_should_create_text(mock_generate_openai_answer):
    expected_text = "Sample joke about topic."
    prompt = "Write a joke about topic."
    mock_response = MagicMock(spec=ChatCompletion)

    mock_choices = MagicMock()
    mock_choices[0].message.content = "Sample joke about topic."

    mock_response.choices = mock_choices
    mock_generate_openai_answer.return_value = mock_response

    assert create_text("topic") == expected_text
    mock_generate_openai_answer.assert_called_once_with(prompt)


@pytest.mark.parametrize("topic", ["chicken", "chicken "])
def test_should_create_prompt(topic):
    from src.joke_api.processing.text.create_text import create_prompt

    expected = "Write a joke about chicken."
    assert create_prompt(topic) == expected
