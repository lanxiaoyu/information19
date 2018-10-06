
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from info import create_app,db
import logging
from flask import current_app

"""
从单一职责的思想考虑：manage.py文件仅仅作为项目启动文件即可，其余配置全部抽取出来"""
app=create_app('development')
#6.创建管理对象
manager = Manager(app)

#7.数据库迁移对象
Migrate(app, db)

#8.添加数据库迁移指令
manager.add_command("db", MigrateCommand)

@app.route('/')
def hello_world():
    logging.debug("This is a debug log.")
    logging.info("This is a info log.")
    logging.warning("This is a warning log.")
    logging.error("This is a error log.")
    logging.critical("This is a critical log.")

    #flask中对logging模块进行封装，直接用current_app调用
    current_app.logger.debug('flask中记录的debug日志')
    return 'hello world777'


if __name__ == '__main__':
   manager.run()