import boto3

from src.joke_api.config import Config
from src.joke_api.helpers.saving_file import save_joke_file

polly_client = boto3.Session(
    aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY,
    region_name=Config.AWS_REGION,
).client("polly")


def generate_audio(text: str, topic: str) -> str:
    extension = Config.AUDIO_EXTENSION
    polly_response = polly_client.synthesize_speech(
        VoiceId="Joanna", OutputFormat=extension, Text=text, Engine="neural"
    )
    with open(f"{topic}.{extension}", "wb") as file:
        file.write(polly_response["AudioStream"].read())

    key = save_joke_file(topic, extension)
    return key
