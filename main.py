from flask import Flask
from entity import *
from api.v1 import user,analysis,grade,upload,util
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///huixue.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

app.register_blueprint(blueprint=user.user_route,url_prefix='/user')
app.register_blueprint(blueprint=analysis.analysis_route,url_prefix='/analysis')
app.register_blueprint(blueprint=grade.grade_route,url_prefix='/grade')
app.register_blueprint(blueprint=upload.upload_route,url_prefix='/upload')
app.register_blueprint(blueprint=util.util_route,url_prefix='/util')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)