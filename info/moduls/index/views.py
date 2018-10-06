import logging
from flask import current_app
from . import index_bp
from info import redis_store

#2、使用蓝图

@index_bp.route('/')
def hello_world():
    #使用redis对象存储kv数据
    redis_store.set("name","durant")
    logging.debug("This is a debug log.")
    logging.info("This is a info log.")
    logging.warning("This is a warning log.")
    logging.error("This is a error log.")
    logging.critical("This is a critical log.")

    #flask中对logging模块进行封装，直接用current_app调用
    current_app.logger.debug('flask中记录的debug日志')
    return 'hello world888'