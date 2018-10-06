from flask import Flask,session
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from config import config_dict

#1、创建app对象
app = Flask(__name__)

configClass=config_dict['development']
#将配置类注册到app上，根据不同配置类，赋予了不同模式的app
app.config.from_object(configClass)

#2、创建数据库对象
db = SQLAlchemy(app)

#3、创建redis数据对象
redis_store=StrictRedis(host=configClass.REDIS_HOST,port=configClass.REDIS_POST,db=configClass.REDIS_NUM)

"""
4、开启csrf保护机制
1、自动获取cookie中的csrf——token，
2、自动获取ajax请求头中的csrf——token
3、自己校验这两个值"""

csrf=CSRFProtect(app)

#5、创建Session对象，将session的存储方法进行调整（flask后端内存--->redis数据库）
Session(app)

#6.创建管理对象
manager = Manager(app)

#7.数据库迁移对象
Migrate(app, db)

#8.添加数据库迁移指令
manager.add_command("db", MigrateCommand)

@app.route('/')
def hello_world():
    return 'hello world777'


if __name__ == '__main__':
   manager.run()