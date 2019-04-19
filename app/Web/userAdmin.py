from flask import render_template, session, request
from flask_login import login_required
from app.datahand.globalmodel.PostModel import PostModel
from app.Web import web
from app.models.DB.mainDB import Post, DB
from app.utlis.xjson import json_success, json_params_error


@web.route("/useradmin/postlist")
@login_required
def userAdminPostList():
    return render_template("UserAdmin/ManagePost/index.html", Model=PostModel().getPostByUid(session["user_id"]))


@web.route("/useradmin/Api/delete", methods=["DELETE"])
@login_required
def userAdmin():
    pid = request.json.get("pid", None)
    userid = session.get("user_id", None)
    postObj = Post.query.filter(Post.pid == pid , Post.uid == userid , Post.flag != 0).first()
    if postObj:
        postObj.flag = 0
        DB.session.commit()
        return json_success("删除成功")
    else:
        return json_params_error("参数错误")
