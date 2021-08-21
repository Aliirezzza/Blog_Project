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


bp = Blueprint("api", __name__, url_prefix="/api")


@bp.route("/categories/")
def categories():
    db = get_db()
    categories = list(db.category.aggregate([
        {'$unwind': '$parent'},
        {'$group': {'_id': '$name', 'parent': {'$push': '$parent'}, 'len': {'$sum': 1}}},
        {'$sort': {'len': 1}}
    ]))
    resp = {'categories': categories}
    print(resp)
    return resp


@bp.route("/tags/")
def tags():
    db = get_db()
    tags = list(db.tag.find())
    for tag in tags:
        tag['_id'] = str(tag['_id'])
    resp = {'tags': tags}
    return resp

@bp.route("post-delete/<post_id>")
@login_required
def post_delete(post_id):
    db = get_db()
    db.post.remove({"_id": ObjectId(post_id)})
    return redirect(url_for("user.posts_list"))

@bp.route("user-profile/<user_id>/", methods=("POST",))
@login_required
def user_profile(user_id):
    db = get_db()
    render_template("user/profile.html", )

@bp.route("/post-deactive/<post_id>/")
@login_required
def post_deactive(post_id):
    db = get_db()
    db.post.update({
        "_id": post_id
        },{
        '$set': {
            "Active": False
            }
        })


@bp.route("/post-active/<post_id>/")
@login_required
def post_active(post_id):
    db = get_db()
    db.post.update({
        "_id": post_id
        }, {
        '$set': {
            "Active": True
            }
        })



