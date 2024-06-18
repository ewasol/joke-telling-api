from unittest.mock import MagicMock, mock_open, patch

from src.joke_api.config import Config
from src.joke_api.processing.audio.generate_audio import generate_audio


@patch("src.joke_api.processing.audio.generate_audio.polly_client")
@patch("src.joke_api.processing.audio.generate_audio.save_joke_file")
@patch("builtins.open", new_callable=mock_open)
def test_generate_audio(mock_open, mock_save_joke_file, mock_polly_client):
    mock_audio_stream = MagicMock()
    mock_audio_stream.read.return_value = b"audio_data"
    mock_polly_response = {"AudioStream": mock_audio_stream}
    mock_polly_client.synthesize_speech.return_value = mock_polly_response
    mock_save_joke_file.return_value = "mocked_key"

    text = "This is a joke"
    topic = "joke_topic"

    result = generate_audio(text, topic)
    assert result == "mocked_key"
    mock_polly_client.synthesize_speech.assert_called_once_with(
        VoiceId="Joanna",
        OutputFormat=Config.AUDIO_EXTENSION,
        Text=text,
        Engine="neural",
    )
    mock_save_joke_file.assert_called_once_with(topic, Config.AUDIO_EXTENSION)
    mock_open.assert_called_once_with(f"{topic}.{Config.AUDIO_EXTENSION}", "wb")
    handle = mock_open()
    handle.write.assert_called_once_with(b"audio_data")
