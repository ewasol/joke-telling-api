from flask import (
    Blueprint,
    Response,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from src.joke_api.models.auth.users import User
from src.joke_api.run import db, login_manager
from src.joke_api.services.auth.forms import LoginForm

auth_bp = Blueprint("auth", __name__)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@auth_bp.route("/login", methods=["GET"])
def login() -> str:
    login_form = LoginForm()
    return render_template("login.html", login_form=login_form)


@auth_bp.route("/login", methods=["POST"])
def login_post() -> Response:
    email = request.form.get("email")
    password = request.form.get("password")
    remember = True if request.form.get("remember") else False

    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        flash("Please check your login details and try again.")
        return redirect(url_for("auth.login"))

    login_user(user, remember=remember)
    return redirect(url_for("views.main"))


@auth_bp.route("/signup")
def signup() -> str:
    return render_template("signup.html")


@auth_bp.route("/signup", methods=["POST"])
def signup_post() -> Response:
    email = request.form.get("email")
    name = request.form.get("name")
    password = request.form.get("password")

    if User.query.filter_by(email=email).first():
        flash("This e-mail address has already been registered.")
        return redirect(url_for("auth.signup"))

    new_user = User(
        email=email,
        name=name,
        password=generate_password_hash(password, method="sha256"),
    )
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for("auth.login"))


@auth_bp.route("/logout")
@login_required
def logout() -> Response:
    logout_user()
    return redirect(url_for("auth.login"))
