import time
import os
import random
import base64
import re

from flask_login import login_required

from app.datahand.Nav_Oklogin import NavOkLoginModel
from . import web
from flask import request, g, session, render_template, redirect, url_for, make_response
from app.models.DB.mainDB import DB, ImgManage, Post, Tag
from app.utlis.xjson import json_params_error, json_success
from app.datahand.globalmodel.ClassfiyModel import ClassfiyModel
from app.datahand.globalmodel.PostModel import PostModel

@web.route("/editor", methods=["POST", "GET"])
# @web.route("/e", methods=["POST", "GET"])
@login_required
def editor():
    userid = session.get("user_id", None)
    if not userid:
        return redirect('web.index')
    model = NavOkLoginModel(userid).Main()
    if request.method == "GET":
        return render_template("EditPost/editindex.html", Model=model,ifshow=True,user_id=userid)
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
            posts.tags.append(i)
        DB.session.add(posts)
        DB.session.commit()

        return json_success("成功", {"url": "post/" + str(posts.pid)})


@web.route("/post/<string:id>", methods=["GET"])
def postShow(id):
    userid = session.get("user_id", None)
    if userid:
        model = NavOkLoginModel(userid).Main()
        return render_template("Post/index.html", Model=model,content=PostModel().getPost(id))
    else:
        return render_template("Post/index.html", Model=ClassfiyModel().GetAllClassfiy(), content=PostModel().getPost(id))

@web.route("/editor/api/classfiyfather", methods=["POST"])
@login_required
def getClassfiyFather():
    return json_success("获取分类", data=ClassfiyModel().getFatherClassfiy())


@web.route("/editor/api/classfiychildren", methods=["POST"])
@login_required
def getClassfiyChildren():
    Id = request.json.get('Id', None)
    if Id:
        return json_success("获取分类", data=ClassfiyModel().getChildrenClassfiy(id=Id))
    return json_params_error("参数错误")


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
