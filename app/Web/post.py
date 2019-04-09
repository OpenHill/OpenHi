import time
import os
import random
import base64
import re

from flask_login import login_required

from app.datahand.Nav_Oklogin import NavOkLoginModel
from . import web
from flask import request, g, session, render_template, redirect, url_for, make_response
from app.form.Editor import EditorForm
from app.models.DB.mainDB import DB, ImgManage, Post
from app.utlis.xjson import json_params_error, json_success
from app.datahand.globalmodel.ClassfiyModel import ClassfiyModel


@web.route("/editor", methods=["POST", "GET"])
# @web.route("/e", methods=["POST", "GET"])
@login_required
def editor():
    userid = session.get("user_id", None)
    model = NavOkLoginModel(userid).Main()
    editorform = EditorForm()
    if request.method == "GET":
        return render_template("EditPost/editindex.html", Model=model)
    else:
        if editorform.validate_on_submit():
            # 数据赋值
            uid = session["user_id"]
            print(request.json)
            return request.json
            # title = editorform.title.data
            # editortext = editorform.editor.data
            #
            # imglist = re.findall('src="(.*?)"', editortext)
            # if imglist:
            #     for i in imglist:
            #         imgneturl = SeveImgAsBase64(i)
            #         editortext = editortext.replace(i, imgneturl)

            # post = Post(uid, title, editortext, )

    # return editortext


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
