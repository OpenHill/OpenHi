from .index import web
from flask import request, render_template, session, redirect, url_for, g, flash, jsonify
from ..models.DB.mainDB import User, DB
from .. import login_manager
from flask_login import login_user, login_required, logout_user
from ..form.LoingandRegnin import LoginFormVal, RegninFormVal
from app.utlis.xjson import json_success, json_params_error


@login_manager.user_loader
def load_user(id):
    return User.query.filter(User.uid == id).first()


@web.route("/login", methods=['GET', 'POST'])
def Login():
    if request.method == "GET":
        return redirect(url_for('Web.index'))
    else:
        login_val = LoginFormVal()
        if login_val.validate_on_submit():
            username = login_val.username.data
            userpwd = login_val.userpwd.data
            user = User.query.filter(User.email == username).first()
            if user:
                if user.check_password(userpwd):
                    login_user(user)
                    session['user_name'] = user.nikename
                    return json_success("登入成功")
                else:
                    return json_params_error("账号或密码错误")
            else:
                return json_params_error("账号或密码错误")
        else:
            error = ""
            if login_val.username.errors:
                error += (login_val.username.errors[0] + ",")
            if login_val.userpwd.errors:
                error += (login_val.userpwd.errors[0] + ",")

        return json_params_error(error)


@web.route('/regnin', methods=['POST', 'GET'])
def regnin():
    if request.method == "GET":
        return redirect(url_for('Web.index'))
    else:
        regnin_val = RegninFormVal()
        if regnin_val.validate_on_submit():
            usernikename = regnin_val.usernikename.data
            username = regnin_val.username.data
            userpwd = regnin_val.userpwd.data
            chackuser = User.query.filter(User.email == username).first()
            if not chackuser:
                user = User(usernikename, username, userpwd, 1)
                DB.session.add(user)
                DB.session.commit()
                login_user(user)
                session['user_name'] = user.nikename
                return json_success("注册成功")
            else:
                return json_params_error("用户已存在")
        else:
            error = ""
            if regnin_val.usernikename.errors:
                error += (regnin_val.usernikename.errors[0] + ",")
            if regnin_val.username.errors:
                error += (regnin_val.username.errors[0] + ",")
            if regnin_val.userpwd.errors:
                error += (regnin_val.userpwd.errors[0] + ",")
    return json_params_error(error)


@web.route("/outlogin", methods=['GET'])
@login_required
def outloing():
    logout_user()
    print(request.referrer)
    return redirect(request.referrer or url_for('Web.index'))

#
