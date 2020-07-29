from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('testForm.html')


@app.route('/load', methods=['GET'])
def load():
    return render_template('load.html')


@app.route('/result', methods=['GET'])
def result():
    return render_template('load.html')


# 录入信息

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    # 登陆之后，判断用户名密码是否正确，从而产生两种跳转
    if username == 'admin' and password == 'password':
        return render_template('testOK.html', username=username)
    # 密码正确，跳转至testOK，把此时键盘获得的username传递给testOK里的username
    return render_template('testForm.html', message='Bad username or password', username=username)
    # 密码错误，跳转至testForm，给予提示，传递参数


if __name__ == '__main__':
    app.run()
