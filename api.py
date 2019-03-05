import tinify
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from api_key import confirmation


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


def get_mail():
    api()


def post_tinyjpg(db):
    access_key = api_keys.query.filter(api_keys.counter != 500).first()
    tinify.key = access_key.key
    print(access_key.key)
    # source = tinify.from_file(uploaded_file)
    access_key.counter = access_key.counter + 1
    db.session.commit()
    # source.to_file(uploaded_file)
    # compressions_this_month = tinify.compression_count


@app.route('/', methods=['GET', 'POST', 'PATCH'])
def main():
    post_tinyjpg(db)
    get_mail()
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True)
