from flask import Flask, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_wtf.csrf import CSRFProtect
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


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

    # redis数据库配置信息
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # 将session存储的数据从内存转移到redis中存储的配置信息
    SECRET_KEY = "SADLKASJDLAKSJDLSAKJD8AS9"
    # 指明数据库类型需要redis数据库
    SESSION_TYPE = "redis"
    # 创建真实存储数据库的对象进行赋值
    SESSION_REDIS = StrictRedis(REDIS_HOST, REDIS_PORT)
    # session_id是否需要进行加密处理
    SESSION_USE_SIGNER = True
    # 设置数据不需要永久保存，而是根据我们设置的过期时长进行调整
    SESSION_PERMANENT = False
    # 设置过期时长 默认数据31天过期
    PERMANENT_SESSION_LIFETIME = 86400


# 1.创建app对象
app = Flask(__name__)
app.config.from_object(Config)

# 2.创建数据库对象
db = SQLAlchemy(app)

# 3.创建redis对象
redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

# 4.给项目添加csrf防护机制
# 提取cookie中的csrf_token
# 如果有表单提取form表单中的csrf_token，如果前端发送的ajax请求从请求头的X-CSRFToken字段中提取csrf_token
# 进行值的比对
CSRFProtect(app)

# 5.将session存储的数据从`内存`转移到`redis`中存储的
Session(app)

# 6.创建管理类
manager = Manager(app)

# 7.创建数据库迁移对象
Migrate(app, db)

# 8.添加迁移指令
manager.add_command("db", MigrateCommand)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    # app.run()
    # 9.使用管理对象运行flask项目
    manager.run()