from flask import Flask, jsonify
from entity import *
from api.v1 import user,analysis,grade,upload,util,api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///huixue.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
api.init_app(app)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)