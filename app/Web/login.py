from .index import web
from flask import request, render_template, session, redirect, url_for, g, flash
from ..models.DB.mainDB import User, DB
from .. import login_manager
from flask_login import login_user, login_required, logout_user
from ..form.LoingandRegnin import LoginFormVal, RegninFormVal


@login_manager.user_loader
def load_user(id):
    return User.query.filter(User.uid == id).first()


@web.route("/login", methods=['GET', 'POST'])
def Login():
    flash("登陆成功", "OK")
    flash("登陆失败", "ERROR")
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
                    next = request.args.get('next')
                    flash("登入成功", "ALLOK")
                    return redirect(next or url_for('api.index'))
                else:
                    flash("密码或账号错误", "Login")
            else:
                flash("不存账号", "Login")
        else:
            if login_val.username.errors:
                flash(login_val.username.errors[0], "Login")
            if login_val.userpwd.errors:
                flash(login_val.userpwd.errors[0], "Login")
        flash("登入失败,错误详情在登陆界面", "ALLNO")
        return redirect(url_for('Web.index'))


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
                next = request.args.get('next')
                return redirect(next or url_for('Web.index'))
            else:
                flash("账号已被注册", "ALLNO")
        else:
            if regnin_val.usernikename.errors:
                flash(regnin_val.usernikename.errors[0], "Regnin")
            if regnin_val.username.errors:
                flash(regnin_val.username.errors[0], "Regnin")
            if regnin_val.userpwd.errors:
                flash(regnin_val.userpwd.errors[0], "Regnin")
    flash("注册失败,错误详情在注册界面", "ALLNO")
    return redirect(url_for('Web.index'))


@web.route("/outlogin", methods=['GET'])
@login_required
def outloing():
    logout_user()
    return redirect(url_for('Web.index'))

@web.route("/s")
def ou():
    return url_for("static",filename="now.html")