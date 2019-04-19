# -*- coding: utf-8 -*
# There is Mr. Wang's creation

from flask import Flask, render_template
from app.models.DB.mainDB import DB
from flask_login import LoginManager
from flask_wtf import CSRFProtect

login_manager = LoginManager()


def create_app(Config):
    # print(Config)
    app = Flask(__name__)

    # 优先导入配置文件
    app.config.from_object(Config)

    CSRFProtect(app)

    register_blueprint(app)

    login_manager.init_app(app)
    login_manager.session_protection = "strong"
    login_manager.login_view = 'Web.index'
    login_manager.login_message_category = 'info'
    login_manager.login_message = 'Access denied.'

    DB.init_app(app)
    with app.app_context():
        # DB.drop_all()
        DB.create_all()

    # error 错定义
    # @app.errorhandler(400)
    # @app.errorhandler(404)
    # def error(error):
    #     code = error.code
    #     if code == 400:
    #         return render_template("Error/400.html"), 400
    #     elif code == 404:
    #         return render_template("Error/404.html"), 404

    errorInit(app)

    return app


def register_blueprint(app):
    ## 注册蓝图 ##
    # 导入蓝图
    from app.Web import web
    from app.User import user
    from app.Api import api
    # 为flask_app 注册蓝图
    app.register_blueprint(web)
    app.register_blueprint(user)
    app.register_blueprint(api)


def errorInit(app):

    @app.errorhandler(400)
    def error400(error):
        return render_template("Error/400.html"), 400

    @app.errorhandler(404)
    def error404(error):
        return render_template("Error/404.html"), 404