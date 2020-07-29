import face_recognition
from flask import Flask, jsonify, request, redirect

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

        if file and allowed_file(file.filename):
            # 图片上传成功，检测图片中的人脸
            return detect_faces_in_image(file)

    # 图片上传失败，输出以下html代码
    return '''
    <!doctype html>
    <title>Bad upload?</title>
    <h1>Upload a picture and see who is in the picture!</h1>
    <form method="POST" enctype="multipart/form-data">
      <input type="file" name="file">
      <input type="submit" value="Upload">
    </form>
    '''


def detect_faces_in_image(file_stream):
    import os
    num = 0
    encoded_list = []

    # 可以读取最多二十张照片进行比较

    def readname():
        filePath = r"/Users/hongxing/cloud computing/face_recognition4gcp/test_photos"
        name = os.listdir(filePath)
        return name

    # 创建一个装有姓名的列表
    name = readname()
    for i in name:
        num = num + 1
        img = face_recognition.load_image_file("test_photos/" + i)
        try:
            img = face_recognition.face_encodings(img)[0]
        except:  # 如果无法从图片中识别到人脸会报错
            pass
        encoded_list.insert(num, img)

    # 载入用户上传的图片
    img = face_recognition.load_image_file(file_stream)
    # 为用户上传的图片中的人脸编码
    unknown_face_encodings = face_recognition.face_encodings(img)[0]

    face_found = False

    if len(unknown_face_encodings) > 0:
        face_found = True
        match_results = face_recognition.compare_faces(encoded_list, unknown_face_encodings[0])
        lables = name

    who = 'No one'

    for i in range(0, len(match_results)):
        if match_results[i] == True:
            who = lables[i]

    # 讲识别结果以json键值对的数据结构输出
    result = {
        "face_found_in_image": face_found,
        "who_is_this": who
    }
    return jsonify(result)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)