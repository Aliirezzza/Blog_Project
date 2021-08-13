from flask import Blueprint
from flask import g
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort
from werkzeug.utils import secure_filename
from bson import ObjectId
from blog.auth import login_required
from blog.db import get_db

bp = Blueprint("user", __name__)


@bp.route("/create", methods=("GET", "POST"))
@login_required
def create_post():
    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
        image = request.form["image"] #??
        category = request.form["category"] #??
        tag = request.form["tag"]
        error = None

        if not title:
            error = "پست شما نیاز به یک اسم دارد."

        if not body:
            error = "شما مطلبی ننوشته اید!!"

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.post.insert_one({"title": title, "body": body, "category": category, "tag": tag, "image_url": image,
                                "author_id": g.user["id"]})
            return redirect(url_for("blog.index"))

    return render_template("user/create_post.html")
