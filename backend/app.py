from flask import Flask ,request

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


if __name__ == '__main__':
    app.run(debug=True)