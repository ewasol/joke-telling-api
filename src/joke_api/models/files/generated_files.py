from src.joke_api.run import db


class GeneratedFiles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("User.id"), nullable=False)
    generated_key = db.Column(db.String(100))

    def __init__(self, user_id: str, generated_key: str) -> None:
        self.user_id = user_id
        self.generated_key = generated_key
