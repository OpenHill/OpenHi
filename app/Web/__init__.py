# -*- coding: utf-8 -*
# There is Mr. Wang's creation
# 蓝图模块化注册文件

# 导入Blueprint

from flask import Blueprint

# 初始化 ‘web’蓝图
web = Blueprint('Web', __name__,
                template_folder="templates")

# 导入视图
from . import index
from . import login
from . import post
from . import filemanage
from .JinJa2_Func import add_global_templates
