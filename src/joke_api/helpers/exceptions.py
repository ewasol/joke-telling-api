from flask import current_app
from werkzeug.exceptions import NotFound

from src.joke_api.config import Config


def raise_if_extension_not_allowed(extension: str) -> None:
    allowed_extensions = [Config.AUDIO_EXTENSION]
    if extension not in allowed_extensions:
        current_app.logger.info("Extension %s not allowed.", extension)
        raise NotFound("extension not allowed")
