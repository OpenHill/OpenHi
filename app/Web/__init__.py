# -*- coding: utf-8 -*
# There is Mr. Wang's creation
# 蓝图模块化注册文件

# 导入Blueprint
from flask import Blueprint

# 初始化 ‘web’蓝图
web = Blueprint('api', __name__)

# 导入视图
from . import index
from . import login
from . import post
from . import filemanage
