from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello world! scdcvsv"

@app.route('/profile')
def profile():
    return "个人中心，profile"

@app.route('/blog/<int:blog_id>')
def blog_id(blog_id):
    return "你访问的是：%s" % blog_id

# 查询字符串形式传参
@app.route('/book/list')
def book_list():
    page = request.args.get("page",default=1,type=int)
    return f"获取第{page}页图书"

# 在app.config中设置好连接数据库的信息
# 然后使用SQLAlchemy(app)创建一个db对象
# SQLAlchemy会自动读取app.config中连接的数据库信息
    # mysql所在主机名
HOSTNAME = "127.0.0.1"
    # mysql监听的端口号
PORT = 3306
    # 链接mysql的用户名，密码，自己设置
USERNAME = "root"
PASSWORD = "250013"

    #mysql 上创建是数据库的名称
DATABASE = "bs_data"

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}"
    # 创建一个对象
db = SQLAlchemy(app)
with app.app_context():
    with db.engine.connect() as conn:
        rs = conn.execute("select 1")
        print(rs.fetchone())


if __name__ == '__main__':
    app.run(debug=True)