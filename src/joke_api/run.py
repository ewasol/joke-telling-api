from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from src.joke_api.config import Config

login_manager = LoginManager()
login_manager.login_view = "auth.login"

db = SQLAlchemy()
migrate = Migrate()


@login_manager.user_loader
def load_user(user):
    from joke_api.models.auth.users import User

    return User.query.get(int(user))


def create_app(mode="DEV") -> Flask:
    from src.joke_api.models.files.generated_files import GeneratedFiles  # noqa

    app = Flask(__name__)
    app.config.from_object(Config)

    login_manager.init_app(app)
    db.init_app(app)
    migrate.init_app(app=app, db=db)

    from src.joke_api.services.auth.views import auth_bp
    from src.joke_api.services.text.views import bp

    app.register_blueprint(bp)
    app.register_blueprint(auth_bp)
    if mode == "TEST":
        create_db(db, app)
    return app


def create_db(db, app):
    with app.app_context():
        db.create_all()
