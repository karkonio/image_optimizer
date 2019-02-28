
from flask import Flask, session, request, flash, send_file
import tinify
import io


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.secret_key = 'secret key'


@app.route('/index', methods=['GET', 'POST'])
def index():
    name = session.get('name')
    return name


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return request.url
        file = request.files['file']
        print(file)
        if file.filename == '':
            flash('No selected file')
            return
        return file
    return 'hello'


def post_tinyjpg(source):
    tinify.key = "0q9Nds6Tc7hR4JyVJSV66dBM6KWPzpgg"
    print(1)
    source_data = source.read()
    print(source_data)
    result_data = tinify.from_buffer(source_data).to_buffer()
    response = io.BytesIO(result_data)
    print(3)
    return response


@app.route('/upload', methods=['POST', 'GET'])
def root():
    img = upload_file()
    img_small = post_tinyjpg(img)
    return send_file(img_small, 'image/jpeg')


if __name__ == '__main__':
    app.debug = True
    app.run()
