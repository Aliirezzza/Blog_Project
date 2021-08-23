import  pymongo
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


@bp.route("/profile")
@login_required
def profile():
    db = get_db()

    return render_template("user/profile.html", title='Profile', )


@bp.route("/posts-list/")
@login_required
def posts_list():
    db = get_db()
    posts = db.post.find({"author_id": ObjectId(g.user["_id"])})
    posts = [post for post in posts]



    return render_template("user/post_list.html", posts=posts)


@bp.route("/create", methods=("GET", "POST"))
@login_required
def create_post():
    if request.method == "POST":
        title = request.form.get('title')
        content = request.form.get('content')
        image = request.form.get('image')  # ????
        category = request.form.get('category')
        tag = request.form.get('tag')
        activition = request.form.get('activition')
        f = request.files.get('image')
        if f:
            fname = secure_filename(f.filename)
            f.save('blog/static/media/' + fname)
            image = fname
        else:
            image = None

        error = None
        if not title:
            error = "پست شما نیاز به یک اسم دارد."

        if not content:
            error = "شما مطلبی ننوشته اید!!"

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.post.insert_one({"title": title, "content": content, "category": category, "tag": tag, "image": image,
                                "activition": activition,
                                "author_username": g.user["username"], "author_id": g.user["_id"],
                                "author_image": g.user["image"]})
            db.post.createIndex({title: 'text', content: 'text', g.user["username"]: 'text'})
            return redirect(url_for("blog.index"))

    return render_template("user/create_post.html")


@bp.route("/edit/<string:post_id>", methods=("GET", "POST"))
@login_required
def edit_post(post_id):
    db = get_db()
    posts = db.post.find({"_id": ObjectId(post_id)})
    li = [p for p in posts]
    post = li[0]

    if request.method == "POST":
        title = request.form.get('title')
        content = request.form.get('content')
        tag = request.form.get('tag')
        activition = request.form.get('activition')

        db.post.update({
            '_id': li[0]['_id']
        }, {
            '$set': {
                "title": title, "content": content, "tag": tag, "activition": activition,
            }
        }, upsert=False, multi=False)
        return redirect(url_for("blog.index"))

    else:
        return render_template("user/edit_post.html", post=post)
