# -*- coding: utf-8 -*
# There is Mr. Wang's creation
import datetime
import time

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Integer, Text, ForeignKey, DateTime, func
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

DB = SQLAlchemy()

# Post_Label 多对多
post_label = DB.Table('post_label',
                      DB.Column("post_id", Integer, ForeignKey("post_table.pid"), primary_key=True),
                      DB.Column("tag_id", Integer, ForeignKey("tag_table.tid"), primary_key=True),
                      )


class User(DB.Model, UserMixin):
    __tablename__ = "user_table"
    uid = DB.Column(Integer, primary_key=True)  # 用户编号
    nikename = DB.Column(String(20), nullable=False)  # 用户昵称
    email = DB.Column(String(50), nullable=False)  # 用户邮箱
    _pwd = DB.Column(String(200), nullable=False)  # 密码
    img = DB.Column(String(200))
    statement = DB.Column(String(300))
    flag = DB.Column(Integer, default=0)  # 匿名用户为 0 / 实名用户为 1 实名可登陆

    def __init__(self, nikename, email, password, flag, img=None, statement=None):
        self.pwd = password
        self.email = email
        self.nikename = nikename
        self.flag = flag
        self.img = img
        self.statement = statement

    def get_id(self):
        try:
            return self.uid
        except AttributeError:
            raise NotImplementedError('No `id` attribute - override `get_id`')

    @property
    def pwd(self):
        return self._pwd

    @pwd.setter
    def pwd(self, password):
        self._pwd = generate_password_hash(password)

    def check_password(self, password):
        resulf = check_password_hash(self.pwd, password)
        return resulf


class Post(DB.Model):
    __tablename__ = "post_table"
    pid = DB.Column(Integer, primary_key=True, autoincrement=True)  # 文章编号
    uid = DB.Column(Integer, ForeignKey("user_table.uid"))  # 发布者
    title = DB.Column(String(50), nullable=False)  # 标题
    content = DB.Column(Text, nullable=False)  # 文章内容
    chacknum = DB.Column(Integer, default=0, nullable=False)  # 点击数量
    tid = DB.Column(Integer, nullable=False)  # 标签便编号  格式: "xxx::xxx"
    cfid = DB.Column(Integer, ForeignKey("classify_table.cfid"), nullable=False)  # 所属类别
    insdate = DB.Column(DateTime, default=func.now())  # 兴建日期
    update = DB.Column(DateTime, default=func.now(), onupdate=func.now())  # 兴建日期
    flag = DB.Column(Integer, default=0)  # 默认为0  0为隐藏/ 1为显示

    tags = DB.relationship('Tag', secondary=post_label, backref=DB.backref('posts'))

    def __init__(self, uid, title, content, lableid, cfid, flag=0):
        self.uid = uid
        self.title = title
        self.content = content
        self.lableid = lableid
        self.cfid = cfid
        self.flag = flag


class Comment(DB.Model):
    __tablename__ = "comment_table"
    cid = DB.Column(Integer, primary_key=True, autoincrement=True)  # 评论编号
    pid = DB.Column(Integer, ForeignKey("post_table.pid"))  # 所属文章
    uid = DB.Column(Integer, ForeignKey("user_table.uid"))  # 谁发的
    text = DB.Column(String(500), nullable=False)  # 评论内容
    nikename = DB.Column(String(20))  # 昵称
    email = DB.Column(String(60))  # 邮箱
    relyuid = DB.Column(Integer, ForeignKey("user_table.uid"))  # 回复谁
    upuid = DB.Column(Integer, ForeignKey("user_table.uid"))  # 在谁的对话下回复
    uptime = DB.Column(DateTime, default=func.now())  # 回复时间
    flag = DB.Column(Integer, default=0)  # 默认为0  0为匿名/ 1为实名


class Tag(DB.Model):
    __tablename__ = "tag_table"
    tid = DB.Column(Integer, primary_key=True, autoincrement=True)  # 标签编号
    postnum = DB.Column(Integer, default=0)  # 下属文章数量
    name = DB.Column(String(20), nullable=False)  # 标签名称


class Classfiy(DB.Model):
    __tablename__ = "classify_table"
    cfid = DB.Column(Integer, primary_key=True, autoincrement=True)  # 分类编号
    cfname = DB.Column(String(60), nullable=False)  # 分类名
    upcfid = DB.Column(Integer)  # 父级分类编号


class ImgManage(DB.Model):
    __tablename__ = "imgmanage_table"
    imgid = DB.Column(Integer, primary_key=True, autoincrement=True)  # 图片编号
    imgname = DB.Column(String(200))
    uid = DB.Column(Integer, ForeignKey("user_table.uid"))  # 谁的图片
    update = DB.Column(DateTime, default=func.now())

    def __init__(self, imgname, uid):
        self.imgname = imgname
        self.uid = uid
