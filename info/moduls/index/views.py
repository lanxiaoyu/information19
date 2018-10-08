import logging
from flask import current_app
from . import index_bp
from info import redis_store
from info.models import User
from flask import render_template
#2、使用蓝图

@index_bp.route('/')
def hello_world():
    return render_template("news/index.html")

@index_bp.route('/favicon.ico')
def favicon():
    """返回网页的图标"""

    return current_app.send_static_file("news/favicon.ico")


