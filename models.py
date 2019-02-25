from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = \
	postgresql://korka:password@127.0.0.1:5000/keys

class API_keys():
	pass
