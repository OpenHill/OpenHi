# -*- coding: utf-8 -*
# There is Mr. Wang's creation
# 蓝图模块化注册文件

# 导入Blueprint
import os

from flask import Blueprint

# 初始化 ‘web’蓝图
user = Blueprint('User', __name__, url_prefix="/user",
                 static_url_path=os.path.join(os.path.dirname(__file__), "static"),
                 template_folder=os.path.join(os.path.dirname(__file__), "template"))

# 导入视图
from . import index
