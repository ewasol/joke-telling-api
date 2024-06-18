import pytest
from mock import MagicMock

from src.joke_api.config import Config
from src.joke_api.models.auth.users import User
from src.joke_api.models.files.generated_files import GeneratedFiles
from src.joke_api.run import login_manager


def create_config():
    Config.SQLALCHEMY_DATABASE_URI = "sqlite:///test_db.db"
    Config.SECRET_KEY = "qwerty"


@pytest.fixture(scope="function")
def app():
    from src.joke_api.run import create_app

    create_config()

    app = create_app(mode="TEST")
    yield app


@pytest.fixture(scope="function")
def client(app):
    return app.test_client()


@pytest.fixture(scope="function")
def logged_in(app):
    app.config.update({"LOGIN_DISABLED": True})
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


@pytest.fixture(scope="module")
def test_user():
    user = User(email="jan@gmail.com", password="password", name="Jan Nowak")
    return user


@pytest.fixture(scope="module")
def test_file():
    file = GeneratedFiles(user_id="111", generated_key="aaaaa")
    return file


@pytest.fixture(scope="module")
def mock_polly_response():
    mock_audio_stream = MagicMock()
    mock_audio_stream.read.return_value = b"audio data"
    mock_response = {"AudioStream": mock_audio_stream}
    return mock_response
