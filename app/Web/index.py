# -*- coding: utf-8 -*
# There is Mr. Wang's creation
# index 视图
from flask_login import logout_user
from . import web
from flask import request, redirect, render_template, session
from ..datahand.Index_Data import IndexData
from app.models.DB.mainDB import User

@web.route('/', methods=['GET', 'POST'])
def index():
    userid = session.get("user_id", None)
    if userid:
        if User.query.filter(User.uid == userid).first():
            model = IndexData(userid).Main()
            return render_template("Index/index.html", Model=model)
        else:
            logout_user()
            return redirect("/")
    else:
        model = IndexData().Main()
        return render_template("Index/index.html", Model=model)



