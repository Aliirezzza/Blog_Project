import pymongo
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

bp = Blueprint("blog", __name__)


@bp.route("/")
@bp.route("/home/")
def index():
    db = get_db()
    posts = db.post.find()
    return render_template('blog/home.html', posts=posts)


@bp.route("/posts/<string:post_id>")
def post_detail(post_id):
    db = get_db()
    post = db.post.find_one({"_id": ObjectId(post_id)})

    if post is None:
        abort(404, f"Post id {post_id} doesn't exist.")

    return render_template("blog/post.html", post=post)

