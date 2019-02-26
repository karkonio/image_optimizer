from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql://postgres:password@localhost:5432/api'
db = SQLAlchemy(app)


class api_keys(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String, unique=True)
    counter = db.Column(db.Integer, unique=False)

    def __init__(self, key, counter):
        self.key = key
        self.counter = counter


# def allowed_file(file):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# def get_img_from_api(file):
#     if request.method == 'GET':
#             # check if the post request has the file part
#             if 'file' not in request.files:
#                 flash('No file part')
#                 return redirect(request.url)
#             else:
#                 uploaded_file = request.files['file']
#                 # if uploaded_file:
#                 # return '.' in filename and \
#                 # filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# def get_mail(key):
#     tm = TempMail()
#     email = tm.get_email_address()  # v5gwnrnk7f@gnail.pw  создаем почту
#     key = tm.get_mailbox(email)  # list of emails получаем письма из почты


# def post_tinyjpg(file, key):
#     tinify.key = "YOUR_API_KEY"
#     source = tinify.from_file(uploaded_file)
#     source.to_file(uploaded_file)
#     # compressions_this_month = tinify.compression_count
#     return


# def get_tinyjpg(file):
#     pass


# def patch_db():
#     pass


@app.route('/', methods=['GET', 'POST', 'PATCH'])
def main():
    return 'Hello, world!'


if __name__ == '__main__':
    app.run(debug=True)
