from mock import MagicMock, patch
from openai import Completion


@patch("src.joke_api.services.text.views.db")
@patch("src.joke_api.services.text.views.generate_audio")
@patch("src.joke_api.processing.text.create_text.generate_openai_answer")
def test_should_generate_and_save_audio_when_logged_in(
    mock_generate_answer, mock_generate_audio, db, client, test_user, app, logged_in
):
    with app.app_context():
        client.post(
            "/login", data={"email": test_user.email, "password": test_user.password}
        )

    text = "Sample joke about chicken"
    prompt = "Write a joke about chicken."
    mock_response = MagicMock(spec=Completion)

    mock_choices = MagicMock()
    mock_choices[0].message.content = "Sample joke about chicken"
    mock_response.choices = mock_choices
    mock_generate_answer.return_value = mock_response

    key = "qwerty"
    mock_generate_audio.return_value = key

    db.session.add = MagicMock()
    db.session.commit = MagicMock()

    get_response = client.get("/audio/chicken")
    mock_generate_answer.assert_called_once_with(prompt)
    assert get_response.status_code == 200
    data = get_response.json
    assert data["text"] == text
    db.session.add.assert_called_once()
    db.session.commit.assert_called_once()
