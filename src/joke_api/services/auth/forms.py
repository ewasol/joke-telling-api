from flask_wtf import FlaskForm
from wtforms import BooleanField, EmailField, PasswordField, SubmitField, validators


class LoginForm(FlaskForm):
    email = EmailField("email", [validators.DataRequired(), validators.Email()])
    password = PasswordField("password", [validators.DataRequired()])
    remember = BooleanField("remember")
    submit = SubmitField("sign in")
