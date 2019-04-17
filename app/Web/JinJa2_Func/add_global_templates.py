# 全局jinja2 变量  #
# http://www.ttlsa.com/python/flask-jinja2-template-engine-global-function/ #
import datetime
import time

from app.Web import web
from app.datahand.globalmodel.ClassfiyModel import ClassfiyModel


@web.app_template_global("jinja_getClassfiyData")
def getClassfiyData():
    return ClassfiyModel().GetAllClassfiy()


@web.app_template_filter("jinja_hanldTime")
def hanldTime(uptime):
    # print(type(Time))
    nowtime = datetime.datetime.now()
    day = (nowtime - uptime).days
    hours = int((nowtime - uptime).seconds / 60 / 60)

    if hours ==0:
        return "刚刚发布"
    if hours <= 24:
        return str(hours) + "小时前"
    if day <= 31:
        return str(day) + "天前"
    return str(int(day /30) + "月前")


if __name__ == '__main__':
    localtime = time.localtime(time.time())
    print(localtime)
