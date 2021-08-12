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
    li = [post for post in posts]
    for post in posts:
        post['_id'] = str(post['_id'])
        print(post['_id'])
        print(post['title'])
        print(post['image'])
        print(post['create_date'])
    return render_template('blog/home.html', posts=li)


@bp.route("/posts/<string:post_id>")
def post_detail(post_id):
    db = get_db()
    post = db.post.find({"_id": ObjectId(post_id)})

    post['_id'] = str(post['_id'])

    if post is None:
        abort(404, f"Post id {post_id} doesn't exist.")

    if post["author"] != g.user["username"]:
        abort(403)

    return render_template("blog/post.html", post=post)

