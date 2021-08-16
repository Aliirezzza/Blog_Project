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
