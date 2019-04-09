# -*- coding: utf-8 -*
# There is Mr. Wang's creation
# 蓝图模块化注册文件

# 导入Blueprint

from flask import Blueprint

# 初始化 ‘web’蓝图
api = Blueprint('Api', __name__,
                template_folder="templates")

# 导入视图

