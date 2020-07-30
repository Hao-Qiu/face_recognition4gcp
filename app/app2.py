import os
import face_recognition
import os
from flask import Flask, jsonify, request, redirect,render_template
import time
from datetime import timedelta

# You can change this to any folder on your system
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__,template_folder='/Users/hao_qiu/Documents/gcp/face_recognition4gcp/templates/templates',\
            static_folder='/Users/hao_qiu/Documents/gcp/face_recognition4gcp/templates/static')
app.config['DEBUG']=True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=6)

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

        #basedir = os.path.abspath(os.path.dirname(__file__))  # 定义一个根目录 用于保存图片用(.py同一个文件夹)
        def editorData():
            imgName = file.filename
            # 定义一个图片存放的位置 存放在static下面
            #path = basedir + "/"
            # 图片path和名称组成图片的保存路径
            file_path = '/Users/hao_qiu/Documents/gcp/face_recognition4gcp/templates/static/pictures_of_people_unknow/unknow.jpg'
            # 保存图片
            file.save(file_path)
            result = os.popen('face_recognition --cpus 5  app/know/ /Users/hao_qiu/Documents/gcp/face_recognition4gcp/templates/static/pictures_of_people_unknow').read() 
            results='The people is \t'+result.split(',')[-1]
            return render_template('result.html', fname=results, var1 = time.time())
        return editorData()
    
    return render_template('predict.html')



# def detect_faces_in_image(file_stream):
#
#     # 讲识别结果以json键值对的数据结构输出
#     result = {
#         "face_found_in_image": face_found,
#         "who_is_this": who
#     }
#     return jsonify(result)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081, debug=True)