# -*- coding: utf-8 -*
# There is Mr. Wang's creation
import datetime
import time

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Integer, Text, ForeignKey, DateTime, func
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

DB = SQLAlchemy()


class User(DB.Model,UserMixin):
    __tablename__ = "user_table"
    uid = DB.Column(Integer, primary_key=True)  # 用户编号
    nikename = DB.Column(String(20), nullable=True)  # 用户昵称
    email = DB.Column(String(50))  # 用户邮箱
    pwd = DB.Column(String(100))  # 密码
    flag = DB.Column(Integer, nullable=1)  # 匿名用户为 0 / 实名用户为 1 实名可登陆

    def get_id(self):
        try:
            return self.uid
        except AttributeError:
            raise NotImplementedError('No `id` attribute - override `get_id`')

class Post(DB.Model):
    __tablename__ = "post_table"
    pid = DB.Column(Integer, primary_key=True, autoincrement=True)  # 文章编号
    uid = DB.Column(Integer,ForeignKey("user_table.uid"))  # 发布者
    title = DB.Column(String(50), nullable=True)  # 标题
    title2 = DB.Column(String(50), nullable=True)  # 副标题
    img = DB.Column(String(500),nullable=True)  # 头图
    content = DB.Column(Text, nullable=True)  # 文章内容
    chacknum = DB.Column(Integer, default=0, nullable=True)  # 点击数量
    lableid = DB.Column(Integer, nullable=True)  # 标签便编号  格式: "xxx::xxx"
    cfid = DB.Column(Integer, ForeignKey("classify_table.cfid"), nullable=True)  # 所属类别
    insdate = DB.Column(DateTime, default=func.now())  # 兴建日期
    update = DB.Column(DateTime, default=func.now(), onupdate=func.now())  # 兴建日期
    flag = DB.Column(Integer, default=0)  # 默认为0  0为隐藏/ 1为显示


class Comment(DB.Model):
    __tablename__ = "comment_table"
    cid = DB.Column(Integer, primary_key=True, autoincrement=True)  # 评论编号
    pid = DB.Column(Integer, ForeignKey("post_table.pid"), nullable=True)  # 所属文章
    uid = DB.Column(Integer, ForeignKey("user_table.uid"))  # 谁发的
    text = DB.Column(String(500), nullable=True)  # 评论内容
    nikename = DB.Column(String(20))  # 昵称
    email = DB.Column(String(60))  # 邮箱
    relyuid = DB.Column(Integer, ForeignKey("user_table.uid"))  # 回复谁
    upuid = DB.Column(Integer, ForeignKey("user_table.uid"))  # 在谁的对话下回复
    uptime = DB.Column(DateTime, default=func.now())  # 回复时间
    flag = DB.Column(Integer, default=0)  # 默认为0  0为匿名/ 1为实名


class Label(DB.Model):
    __tablename__ = "lable_table"
    lid = DB.Column(Integer, primary_key=True)  # 标签编号
    postnum = DB.Column(Integer, default=0)  # 下属文章数量
    name = DB.Column(String(20), nullable=True)  # 标签名称


class Classify(DB.Model):
    __tablename__ = "classify_table"
    cfid = DB.Column(Integer, primary_key=True)  # 分类编号
    cfname = DB.Column(String(60), nullable=True)  # 分类名
    upcfid = DB.Column(Integer)  # 父级分类编号

