import functools

from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

from blog.db import get_db

bp = Blueprint("auth", __name__, url_prefix="/auth")


def login_required(view):
    """View decorator that redirects anonymous users to the login page."""

    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))

        return view(**kwargs)

    return wrapped_view


@bp.before_app_request
def load_logged_in_user():
    """If a user id is stored in the session, load the user object from
    the database into ``g.user``."""
    username = session.get("username")

    if username is None:
        g.user = None
    else:
        g.user = (
            
            get_db().user.find_one({"username":username})
        )


@bp.route("/signup", methods=("GET", "POST"))
def signup():
    """Register a new user.
    Validates that the username is not already taken. Hashes the
    password for security.
    """
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        mobile = request.form["mobile"]
        username = request.form["username"]
        password = request.form["password"]
        f = request.files.get('image')
        if f:
            fname = secure_filename(f.filename)
            f.save('blog/static/media/' + fname)
            image = fname
        else:
            image = None
        db = get_db()
        error = None

        if not username:
            error = "Username is required."
        elif not password:
            error = "Password is required."
        elif (
            
            db.user.find_one({"username":username})
            is not None
        ):
            error = f"User {username} is already registered."

        if error is None:
            user={"first_name":first_name,"last_name":last_name,"mobile":mobile,"email":email,"image":image,"username":username,"password":generate_password_hash(password)}
            db.user.insert_one(user)
            return redirect(url_for("auth.login"))

        flash(error)
    return render_template("auth/signup.html")


@bp.route("/login", methods=("GET", "POST"))
def login():
    """Log in a registered user by adding the user id to the session."""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        db = get_db()
        error = None
       
        user=db.user.find_one({"username":username})
        print(user)
        if user is None:
            error = "Incorrect username."
        elif not check_password_hash(user["password"], password):
            error = "Incorrect password."

        if error is None:
            # store the user id in a new session and return to the index
            session.clear()
            session["username"] = user["username"]
            return redirect(url_for("home"))

        flash(error)
        print(error)
    return render_template("auth/login.html")


@bp.route("/logout")
def logout():
    """Clear the current session, including the stored user id."""
    session.clear()
    return redirect(url_for("home"))
