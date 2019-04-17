import time
import os
import random
import base64
import re

from flask_login import login_required

# from app.datahand.Nav_Oklogin import NavOkLoginModel,NavOnLoginModel
from app.datahand.globalmodel.CommentModel import CommentModel
from . import web
from flask import request, g, session, render_template, redirect, url_for
from app.models.DB.mainDB import DB, ImgManage, Post, Tag, Comment
from app.utlis.xjson import json_params_error, json_success
from app.datahand.globalmodel.ClassfiyModel import ClassfiyModel
from app.datahand.globalmodel.PostModel import PostModel


@web.route("/post/editor", methods=["POST", "GET"])
@login_required
def editor():
    userid = session.get("user_id", None)
    if not userid:
        return redirect('web.index')
    if request.method == "GET":
        return render_template("EditPost/editindex.html", ifshow=True)
    else:
        postTitle = request.json.get("postTitle", "未命名")
        postContent = request.json.get("postContent", None)
        postTags = request.json.get("postTags", None)
        postClassfiy = request.json.get("postClassfiy", None)

        if not postContent:
            return json_params_error("内容都敢为空？？？")
        if not postTags:
            return json_params_error("标记都没有？？？")
        if not postClassfiy:
            return json_params_error("不分类吗？？？")

        postTags = postTags.split(":")[1:]

        # Tag逻辑
        for index, i in enumerate(postTags):
            tag = Tag.query.filter(Tag.name == i).first()
            if not tag:
                newtag = Tag(i)
                DB.session.add(newtag)
                DB.session.commit()
                postTags[index] = newtag
            else:
                postTags[index] = tag

        # PostContent逻辑
        imglist = re.findall('src="(.*?)"', postContent)
        if imglist:
            for i in imglist:
                imgneturl = SeveImgAsBase64(i)
                postContent = postContent.replace(i, imgneturl)

        posts = Post(userid, postTitle, postContent, postClassfiy)
        for i in postTags:
            posts.tag.append(i)
        DB.session.add(posts)
        DB.session.commit()

        return json_success("成功", {"url": "/post?pid=" + str(posts.pid)})


@web.route("/post", methods=["GET"])
def postShow():
    userid = session.get("user_id", None)
    pid = request.args.get("pid", None)

    # 访问+1
    cmt = Post.query.filter(Post.pid == pid).first()
    cmt.chacknum = cmt.chacknum + 1
    DB.session.commit()

    commentmodel = CommentModel().getAllComment(pid)
    if not pid:
        return redirect(request.args.get('next', url_for('Web.index')))
    if userid:
        # model = NavOkLoginModel(userid).Main()
        return render_template("Post/index.html", content=PostModel().getPost(pid),
                               commentlist=commentmodel)
    else:
        return render_template("Post/index.html",
                               content=PostModel().getPost(pid), commentlist=commentmodel)


@web.route("/post/editor/api/classfiyfather", methods=["POST"])
@login_required
def getClassfiyFather():
    return json_success("获取分类", data=ClassfiyModel().getFatherClassfiy())


@web.route("/post/editor/api/classfiychildren", methods=["POST"])
@login_required
def getClassfiyChildren():
    Id = request.json.get('Id', None)
    if Id:
        return json_success("获取分类", data=ClassfiyModel().getChildrenClassfiy(id=Id))
    return json_params_error("参数错误")


@web.route("/post/comment", methods=["POST"])
def postComment():
    name = request.json.get("Name")
    uid = request.json.get("Uid")
    cid = request.json.get("Cid")
    upcid = request.json.get("Upcid")
    pid = request.json.get("Pid")
    content = request.json.get("Content")

    if not name:
        return json_params_error("必须要昵称")
    if not content or len(content) <= 8:
        return json_params_error("无评论内容")
    if not cid:
        return json_params_error("参数错误")
    if not uid:
        return json_params_error("参数错误")
    if not upcid:
        return json_params_error("参数错误")
    if not pid:
        return json_params_error("参数错误")

    comment = Comment(pid=pid,
                      uid=uid if uid != "0" else None,
                      text=content,
                      relycid=cid if cid != "0" else None,
                      upcid=upcid if upcid != "0" else None,
                      nikename=name
                      )
    DB.session.add(comment)
    DB.session.commit()

    return json_success("ok")


#  工具方法


def SeveImgAsBase64(basecode):
    """
    :param bsaecode: bs64字符串
    :return: 返回URL地址
    """
    # 随机名字,获取尾缀
    imgname = "{0}.{1}".format(int(time.time()) + random.randint(1000, 80000), basecode[11:].split(";")[0])
    # 当前文件的文件夹
    basepath = os.path.dirname(os.path.dirname(__file__))
    # 拼接保存文件路径
    upload_path = os.path.join(basepath, "static", "uploads", "img", imgname)
    # 保存文件
    with open(upload_path, "wb") as f:
        # 切割bs64
        pattern = re.compile(r"^(data:\s*image\/(\w+);base64,)")
        bstext = re.sub(pattern, "", basecode)
        # 写入文件
        f.write(base64.b64decode(bstext))

    # 加入图片管理数据库
    imgobj = ImgManage(imgname, session["user_id"])
    DB.session.add(imgobj)
    DB.session.commit()

    # 放回图片的网络地址
    return "/file/img/" + imgname
