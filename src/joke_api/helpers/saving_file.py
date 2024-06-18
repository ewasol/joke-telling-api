import base58
import boto3

from src.joke_api.config import Config
from src.joke_api.helpers.exceptions import raise_if_extension_not_allowed


def save_joke_file(topic: str, file_extension: str) -> str:
    raise_if_extension_not_allowed(file_extension)
    base_key = base58.b58encode(topic.encode("utf-8")).decode("utf-8")

    s3 = boto3.client(
        "s3",
        region_name=Config.AWS_REGION,
        aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY,
    )
    s3.upload_file(
        Filename=f"{topic}.{file_extension}",
        Bucket=Config.AUDIO_BUCKET,
        Key=f"{base_key}.{file_extension}",
    )
    return base_key
