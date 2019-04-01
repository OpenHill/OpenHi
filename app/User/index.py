from . import user
from flask import render_template


@user.route("/")
def n():
    return render_template("new.html")
