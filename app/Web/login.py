from .index import web
from flask import request, render_template, session, redirect, url_for
from ..models.DB.mainDB import User
from ..models import DB
from .. import login_manager
from flask_login import login_user, login_required,logout_user


@login_manager.user_loader
def load_user(id):
    return User.query.filter(User.uid == id).first()


@web.route("/login", methods=['GET', 'POST'])
def Login():
    if request.method == "GET":
        return redirect(url_for('api.index'))
    else:
        username = request.form["username"]
        userpwd = request.form["userpwd"]
        user = User.query.filter(User.email == username, userpwd == User.pwd).first()
        if user:
            login_user(user)
            next = request.args.get('next')
            return redirect(next or url_for('api.index'))
        else:
            return redirect(url_for('api.index'))


@web.route('/regnin', methods=['POST'])
def regnin():
    pass

@web.route("/outlogin", methods=['GET'])
@login_required
def outloing():
    logout_user()
    return redirect(url_for('api.index'))


