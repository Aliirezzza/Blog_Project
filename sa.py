from bson import ObjectId

@bp.route("/")
@bp.route("/home/")
def index():
    db = get_db()
    posts = db.posts.find().sort({"date_created": -1})
    for post in posts:
        post['_id'] = str(post['_id'])
    return render_template('blog/home.html', posts=posts)


@bp.route("posts/<string:post_id>")
def post_detail(post_id):
    db = get_db()
    post = db.posts.find({"_id": ObjectId(post_id)})

    post['_id'] = str(post['_id'])

    if post is None:
        abort(404, f"Post id {post_id} doesn't exist.")

    if post["author"] != g.user["username"]:
        abort(403)

    return render_template("blog/post.html", post=post)