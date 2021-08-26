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
    categories = list(db.category.find())
    for category in categories:
        category['_id'] = str(category['_id'])
    resp = {'categories': categories}
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

# like api
@bp.route('/like/<post_id>')
@login_required
def like(post_id):
    db = get_db()
    posts = list(db.post.find({"_id": ObjectId(post_id)}))
    post = posts[0]

    like = post['like']
    dislike = post['dislike']
    # if request.method == 'POST':
    if g.user["username"] not in like:        #  user not already like post this state for pervent one user like twice
        if g.user["username"] not in dislike: #  user not already dislike post  this state for pervent one user like and dislike concurrent
            like.append(g.user["username"])
            db.post.update(
                {'_id': post['_id']},
                {'$set': {"like": like,}},
                upsert=False, multi=False)
            return {"status": 1}
        else:
            dislike.remove(g.user["username"])
            like.append(g.user["username"])
            db.post.update(
                {'_id': post['_id']},
                {'$set': {"like": like, "dislike": dislike, }},
                upsert=False, multi=False)
            return {"status": 2}
    else:
        like.remove(g.user["username"])
        db.post.update(
            {'_id': post['_id']},
            {'$set': {"like": like, }},
            upsert=False, multi=False)
        return {"status": 3}


#dislike api
@bp.route('/dislike/<post_id>')
@login_required
def dislike(post_id):
    db = get_db()
    posts = list(db.post.find({"_id": ObjectId(post_id)}))
    post = posts[0]

    like = post['like']
    dislike = post['dislike']
    # if request.method == 'POST':
    if g.user["username"] not in dislike:     #  user not already dislike post this state for pervent one user like twice
        if g.user["username"] not in like:    #  user not already like post  this state for pervent one user like and dislike concurrent
            dislike.append(g.user["username"])
            db.post.update(
                {'_id': post['_id']},
                {'$set': {"dislike": dislike, }},
                upsert=False, multi=False)
            return {"status": 1}
        else:
            like.remove(g.user["username"])
            dislike.append(g.user["username"])
            db.post.update(
                {'_id': post['_id']},
                {'$set': {"like": like, "dislike": dislike, }},
                upsert=False, multi=False)
            return {"status": 2}
    else:
        dislike.remove(g.user["username"])
        db.post.update(
            {'_id': post['_id']},
            {'$set': {"dislike": dislike, }},
            upsert=False, multi=False)
        return {"status": 3}





