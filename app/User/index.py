from app.models.DB.mainDB import Post, User
from . import user
from flask import render_template


@user.route("/")
def n():
    postlist = Post.query.filter().first()
    print(postlist.user.nikename)

    userlist = User.query.filter().first()
    print(userlist.post)
    return "app"
