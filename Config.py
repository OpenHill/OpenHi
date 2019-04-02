# -*- coding: utf-8 -*
# There is Mr. Wang's creation
class Config:
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:Wang20000128.@173.82.240.123/openhi"
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Wang20000128.@127.0.0.1/openhi?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    CSRF_ENABLED = True

    SECRET_KEY = "sdaskdhjasohd[;/;paaiohd+-aioush"

    # 调试状态

    DEBUG = True
