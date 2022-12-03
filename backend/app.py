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

# 测试是否连接成功
# with app.app_context():
#     with db.engine.connect() as conn:
#         rs = conn.execute("select 1")
#         print(rs.fetchone())
class User(db.Model):
    __tablename__ ="user"
    id = db.Column(db.Integer , primary_key=True,autoincrement=True)
    # db.string()映射成varchar类型
    username = db.Column(db.String(100),nullable=False)
    password = db.Column(db.String(100), nullable=False)

# user = User(username = "法外狂徒张三",password="11111111")
# 对应sql语句：insert user(username,password) values('法外狂徒张三'，’11111111‘)

with app.app_context():
    db.create_all()
    # 将表同步到数据库中去
@app.route("/user/add")
def add_user():
    # 1.创建user对象
    user = User(username="法外狂徒张三", password="11111111")
    # 2.将ORM对象添加到db.session中
    db.session.add(user)
    # 3.将db.session中的改变同步到数据中，commit
    db.session.commit()
    return "用户添加成功"

# 查询
@app.route("/user/query")
def query_user():
    # 1.get查找，根据主键
    user = User.query.get(1)
    # print(f"{user.id}——{user.password}--{user.username}")
    #filter_by查找
    users = User.query.filter_by(username = "法外狂徒张三")
    # users为Query对象：类数组
    for user in users:
        print(user.username)
    return "数据查找成功!"

# 更新
@app.route("/user/update")
def update_user():
    user = User.query.filter_by(username="法外狂徒张三").first()
    user.password = "88888888"
    db.session.commit()
    return "数据修改成功！"
# 删除
@app.route("/user/delete")
def delete_user():
    # 1.查找
    user = User.query.filter_by(username="法外狂徒张三").first()
    # 2.从db.session中删除
    db.session.delete(user)
    # 将db.session中的删除同步到数据库中
    db.session.commit()
    return "数据删除成功！"



if __name__ == '__main__':
    app.run(debug=True)