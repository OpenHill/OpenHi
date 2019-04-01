import os

from . import web
from flask import Response


@web.route("/file/img/<string:name>")
def getImg(name):
    mdict = {
        'jpeg': 'image/jpeg',
        'jpg': 'image/jpeg',
        'png': 'image/png',
        'gif': 'image/gif'
    }
    basepath = os.path.dirname(os.path.dirname(__file__))
    localurl = os.path.join(basepath, "static", "uploads", "img", name)
    ishave = os.path.exists(localurl)
    if ishave:
        with open(localurl, "rb") as f:
            img = f.read()

        return Response(img, mimetype=mdict[((localurl.split('/')[-1]).split(".")[1])])
