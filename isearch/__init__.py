# coding:utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint

api = Blueprint("api", __name__)

# 数据库
db = SQLAlchemy()

# coding:utf-8
class Config(object):
    """配置信息"""
    SECRET_KEY = "XHSOI*Y9dfs9cshd9"

    # 数据库
    SQLALCHEMY_DATABASE_URI = "mysql://root:HeHe_Qwui30125@192.168.0.92:3306/isearch"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    DEBUG = True


# 工厂模式
def create_app():
    """
    创建flask的应用对象
    :param config_name: str  配置模式的模式的名字 （"develop",  "product"）
    :return:
    """
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(api, url_prefix="/")

    return app
