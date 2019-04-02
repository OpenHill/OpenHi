# -*- coding: utf-8 -*
# There is Mr. Wang's creation
# index 视图
from flask_wtf import FlaskForm

from . import web
from flask import request, redirect, render_template, session
from ..datahand.Index_Data import IndexData
from ..form.LoingandRegnin import LoginFormVal, RegninFormVal


@web.route('/', methods=['GET', 'POST'])
def index():
    userid = session.get("user_id", None)
    if userid:
        model = IndexData(userid).Main()
        return render_template("Oklogin/index.html", Model=model)
    else:
        LoginForm = LoginFormVal()
        RegninForm = RegninFormVal()
        model = IndexData().Main()
        return render_template("Nologin/index.html", Model=model, loginforms=LoginForm, regninforms=RegninForm)
