from flask_login import UserMixin

from src.joke_api.run import db


class User(UserMixin, db.Model):
    __tablename__ = "User"
    __table_args__ = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    generated_files = db.relationship("GeneratedFiles", backref="user", uselist=True)

    def __init__(self, email: str, password: str, name: str) -> None:
        self.email = email
        self.password = password
        self.name = name
