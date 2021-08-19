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


@bp.route("/category-posts/<string:category_name>/")
def category(category_name):
    db = get_db()
    posts = db.post.find({"category": category_name})
    return render_template("blog/category.html", posts=posts)


@bp.route("/tag-posts/<string:tag_name>/")
def tag(tag_name):
    db = get_db()
    posts = db.post.find({"tag": tag_name})
    return render_template("blog/tag.html", posts=posts)

