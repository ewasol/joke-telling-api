from unittest.mock import MagicMock

from mock import patch
from openai import ChatCompletion


@patch("src.joke_api.processing.text.create_text.generate_openai_answer")
def test_should_return_text_when_logged_in(
    mock_generate_answer, client, app, logged_in
):
    with app.app_context():
        client.post(
            "/login", data={"username": "test_user", "password": "test_password"}
        )
        text = "Sample joke about chicken."
        prompt = "Write a joke about chicken."
        mock_openai_response = MagicMock(spec=ChatCompletion)

        mock_choices = MagicMock()
        mock_choices[0].message.content = text

        mock_openai_response.choices = mock_choices
        mock_generate_answer.return_value = mock_openai_response

        response = client.get("/text/chicken")
        actual_status_code = response.status_code
        mock_generate_answer.assert_called_once_with(prompt)
        expected_status_code = 200
        assert response.get_json() == text
        assert actual_status_code == expected_status_code


def test_should_redirect_to_login_when_not_logged_in(client):
    response = client.get("/text/chicken")
    actual_status_code = response.status_code
    expected_status_code = 302
    assert actual_status_code == expected_status_code
    assert "/login" in response.headers["Location"]
