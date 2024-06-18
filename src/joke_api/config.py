import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    OPENAI_KEY = os.getenv("OPENAI_KEY", "TEST_VALUE")
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_REGION = os.getenv("AWS_REGION")
    AUDIO_BUCKET = os.getenv("AUDIO_BUCKET")
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    SECRET_KEY = os.getenv("SECRET_KEY")
    MODEL = "gpt-3.5-turbo"
    AUDIO_EXTENSION = "mp3"
