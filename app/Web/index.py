# -*- coding: utf-8 -*
# There is Mr. Wang's creation
# index 视图
from . import web
from flask import request, redirect, render_template, session
from ..datahand.NoLogin_Index_Data import NoLoginIndexData
from ..form.LoingandRegnin import LoginFormVal


@web.route('/', methods=['GET', 'POST'])
def index():
    userid = session.get("user_id", None)
    if userid:
        return render_template("Oklogin/index.html")
    else:
        LoginForm = LoginFormVal()
        model = NoLoginIndexData().Mian()
        return render_template("Nologin/index.html", Model=model, forms=LoginForm)
