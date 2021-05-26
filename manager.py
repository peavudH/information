from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# 0.自定义项目配置类
class Config(object):
    """项目配置类"""

    # 开启debug模式
    DEBUG = True

    # mysql数据库配置信息
    # mysql数据库链接配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:xiaoxiaozi@127.0.0.1:3306/information21"
    # 开启数据库跟踪操作
    SQLALCHEMY_TRACK_MODIFICATIONS = True



# 1.创建app对象
app = Flask(__name__)
app.config.from_object(Config)

# 2.创建数据库对象
db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()