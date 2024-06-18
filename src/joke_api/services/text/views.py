import io
import json
from typing import Tuple

import boto3
from flask import Blueprint, Response, jsonify, make_response, send_file
from flask_login import current_user, login_required

from src.joke_api.config import Config
from src.joke_api.models.files.generated_files import GeneratedFiles
from src.joke_api.processing.audio.generate_audio import generate_audio
from src.joke_api.processing.text.create_text import create_text
from src.joke_api.run import db

bp = Blueprint("views", __name__)


@bp.route("/main", methods=["GET"])
@login_required
def main() -> Tuple[Response, int]:
    message = (
        "Hello! Choose a funny topic and I'll tell you a joke about it. You "
        "can have it in text or audio format!"
    )
    return jsonify(message), 200


@bp.route("/text/<string:topic>", methods=["GET"])
@login_required
def get_intro(topic: str) -> Tuple[Response, int]:
    text = create_text(topic)
    return jsonify(text), 200


@bp.route("/audio/<string:topic>", methods=["GET"])
@login_required
def get_audio(topic: str) -> Tuple[dict, int]:
    text = create_text(topic)
    key = generate_audio(text, topic)
    user_id = current_user.get_id()
    generated_file = GeneratedFiles(user_id, key)
    db.session.add(generated_file)
    db.session.commit()
    return {"text": text, "key": key}, 200


@bp.route("/download/<string:key>", methods=["GET"])
@login_required
def download_audio(key: str) -> Response | Tuple[str, int]:
    user_id = current_user.get_id()
    if GeneratedFiles.query.filter_by(user_id=user_id, generated_key=key).count() > 0:
        s3 = boto3.client(
            "s3",
            region_name=Config.AWS_REGION,
            aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY,
        )
        buf = io.BytesIO()
        extension = Config.AUDIO_EXTENSION
        s3.download_fileobj(Config.AUDIO_BUCKET, f"{key}.{extension}", buf)
        buf.seek(0)
        return send_file(
            buf,
            download_name=f"{key}.{extension}",
            mimetype="audio/mpeg",
        )
    return "You are not allowed to download the file.", 403


@bp.route("/healthz")
def get_health() -> Response:
    response = make_response(json.dumps({"status": "OK"}))
    return response
