
from flask import Flask, session, request, send_file, Response
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
        file = request.files['file']
        if file and allowed_file(file.filename):
            return file
    return 'Hello'


def post_tinyjpg(source):
    tinify.key = "qw0KN22581F0k15PbYRyr8jpGzdf20w9"
    source_data = source.read()
    result_data = tinify.from_buffer(source_data).to_buffer()
    response = io.BytesIO(result_data)
    response.filename = source.filename
    return response


@app.route('/upload', methods=['POST', 'GET'])
def root():
    if 'file' not in request.files:
        try:
            return Response('No file part',
                            status=422,
                            mimetype='application /json')
        except Exception:
            pass
    else:
        try:
            img = upload_file()
            img_small = post_tinyjpg(img)
            return send_file(img_small, attachment_filename=img_small.filename)
        except Exception:
            return Response('Picture format is not correct',
                            status=422,
                            mimetype='application /json')


if __name__ == '__main__':
    app.debug = True
    app.run()
