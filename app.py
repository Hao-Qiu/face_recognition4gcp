import os
from flask import Flask, jsonify, request, redirect, render_template

# You can change this to any folder on your system
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_image():
    # 检测图片是否上传成功
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            return redirect(request.url)

        basedir = os.path.abspath(os.path.dirname(__file__))  # 定义一个根目录 用于保存图片用(.py同一个文件夹)
        def editorData():
            imgName = "000.jpg"
            path = basedir + "/"
            # 图片path和名称组成图片的保存路径
            file_path = path + imgName
            # 保存图片
            file.save(file_path)
        #     通过img_stream实现本地图片输出前端
            return render_template('index.html',
                                   file = file)
        # return editorData() # 返回后端url
        return editorData()

    # 图片上传失败，输出以下html代码
    return '''
    <!doctype html>
    <title>Who is it?</title>
    <h1>Upload a picture and see who that is!</h1>
    <form method="POST" enctype="multipart/form-data">
      <input type="file" name="file">
      <input type="submit" value="Upload">
    </form>
    '''

# def detect_faces_in_image(file_stream):
#
#     # 讲识别结果以json键值对的数据结构输出
#     result = {
#         "face_found_in_image": face_found,
#         "who_is_this": who
#     }
#     return jsonify(result)

# 调用shell进行face recognition
def output():
    v_return_status = os.system('sh face_rec.sh')
    return str(v_return_status)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)