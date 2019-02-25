from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
# from tempmail import TempMail
from models import db


# ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)


POSTGRES = {
    'user': 'postgres',
    'pw': 'password',
    'db': 'keys',
    'host': 'localhost',
    'port': '5000',
}
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://%(user)s:\
    %(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
db.init_app(app)

"""
# def allowed_file(file):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def get_img_from_api(file):
    if request.method == 'GET':
            # check if the post request has the file part
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            else:
                uploaded_file = request.files['file']
                # if uploaded_file:
                # return '.' in filename and \
                # filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def get_mail(key):
    tm = TempMail()
    email = tm.get_email_address()  # v5gwnrnk7f@gnail.pw  создаем почту
    key = tm.get_mailbox(email)  # list of emails получаем письма из почты


def post_tinyjpg(file, key):
    tinify.key = "YOUR_API_KEY"
    source = tinify.from_file(uploaded_file)
    source.to_file(uploaded_file)
    # compressions_this_month = tinify.compression_count
    return


def get_tinyjpg(file):
    pass


def patch_db():
    pass
"""

@app.route('/', methods=['GET', 'POST', 'PATCH'])
def main():
    return 'Hello, world!'
        # img = get_img_from_api()
        # mail = get_mail()
        # tinyjpg = post_tinyjpg()
        # key = patch_db()
        # send_img = send_img_to_api()


if __name__ == '__main__':
    app.run(debug=True)
