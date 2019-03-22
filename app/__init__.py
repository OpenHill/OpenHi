# -*- coding: utf-8 -*
# There is Mr. Wang's creation

from flask import Flask
from app.models.DB.mainDB import DB
from flask_login import LoginManager

login_manager = LoginManager()

def create_app(Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    register_blueprint(app)
    login_manager.init_app(app)
    login_manager.session_protection = "strong"
    login_manager.login_view = 'api.index'
    login_manager.login_message_category = 'info'
    login_manager.login_message = 'Access denied.'
    DB.init_app(app)
    with app.app_context():
        # DB.drop_all()
        DB.create_all()
    return app
def register_blueprint(app):
    ## 注册蓝图 ##
    # 导入蓝图
    from app.Web import web

    #为flask_app 注册蓝图
    app.register_blueprint(web)


