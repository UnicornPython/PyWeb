from flask import Flask, render_template, request, redirect

# 引入 Flask
app = Flask(__name__)


# 直接返回文本内容
# =======================================================
@app.route("/")
def index():
    # .
    return """
        <h1>中国联通</h1>
        <hr/>
        <h6>中国移动</h6>
    """

# 借助模板返回内容
# 模板的固定的文件夹在根目录下 templates 文件夹中
# 静态文件放在根文件夹下的 static 文件夹中
# =======================================================
@app.route("/home")
def home():
    return render_template("home/index.html")


# 在模板中添加返回的数据,动态组装
@app.route("/profile")
def profile():
    return render_template(
        "profile/index.html", 
        username="alex",
        avatar="/static/images/avatar.png",
        hobby=['vollyball',"basketball", "swimming"],
        info={"birthday": "2023-02-29", "identify": "student","luck": "1,9,6,8" }
    )



# 多种请求方法(默认没有备注的时候为`GET`请求) 
# ========================================================
@app.route("/register", methods = ['GET', "POST"])
def register():
    # 获取请求的方法
    method = request.method
    if method == "GET":
        # 获取 url 参数
        now = request.args.get("time")
        print("收到客户注册请求", now)
        return render_template("register/index.html", data = now)
    elif method == "POST":
        # 获取表单参数
        username = request.form.get("username")
        password = request.form.get("password")
        # 获取多选框的参数是需要使用 getlist() 方法
        print(f"{username},{password}")
        return "ok"


# 请求重定向
# ===========================================================
@app.route("/redict")
def go_baidu():
    return redirect("https://baidu.com")



# 从当前模块，以 app 配置监听当前机器的 9999 端口
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=9999)
