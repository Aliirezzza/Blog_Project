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

@bp.route("/create", methods=("GET", "POST"))
@login_required
def create():
    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
        image = request.form["image"]
        category = request.form["category"]
        tag = request.form["tag"]
        error = None

        if not title:
            error = "Title is required."

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.post.insert_one({"title": title, "body": body, "category": category, "tag": tag, "image_url": image, "author_id": g.user["id"]})
            return redirect(url_for("blog.index"))

    return render_template("user/create_post.html")


# @bp.route("/<int:id>/update", methods=("GET", "POST"))
# @login_required
# def update(post_id):
#     """Update a post if the current user is the author."""
#
#
#     if request.method == "POST":
#         title = request.form["title"]
#         body = request.form["body"]
#         image = request.form["image"]
#         category = request.form["category"]
#         tag = request.form["tag"]
#         error = None
#
#         if not title:
#             error = "Title is required."
#
#         if error is not None:
#             flash(error)
#         else:
#             db = get_db()
#             db.post.updateOne({
#                 "_id" : post_id
#             }, {
#                     $set :{
#                     title: title,
#                     body : body,
#                     image_url : image,
#                     category : category,
#                     tag : tag
#                     }
#                 })
#             # db.execute(
#             #     "UPDATE post SET title = ?, body = ?, image_url = ?, category = ?, tag = ?, WHERE id = ?",
#             #     (title, body, image, category, tag, id)
#             # )
#             # db.commit()
#             return redirect(url_for("blog.index"))
#
#     return render_template("blog/post.html", post=post)


@bp.route("/<int:id>/delete", methods=("POST",))
@login_required
def delete(post_id):
    db = get_db()
    db.post.remove({post_id});

    return redirect(url_for("blog.index"))
