from flask import Flask, jsonify
from entity import *
from api.v1 import user,analysis,grade,upload,util
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///huixue.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
SWAGGER_URL = '/api/docs'
API_URL = '/swagger.json'
# 创建 Swagger UI 蓝图
swaggerui_blueprint = get_swaggerui_blueprint(
SWAGGER_URL,
API_URL,
config={
'app_name': "Test application"
}
)
@app.route('/swagger.json')
def swagger_docs():
    swag = swagger(app)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "Huixue API"
    return jsonify(swag)
app.register_blueprint(blueprint=user.user_route,url_prefix='/user')
app.register_blueprint(blueprint=analysis.analysis_route,url_prefix='/analysis')
app.register_blueprint(blueprint=grade.grade_route,url_prefix='/grade')
app.register_blueprint(blueprint=upload.upload_route,url_prefix='/upload')
app.register_blueprint(blueprint=util.util_route,url_prefix='/util')
app.register_blueprint(swaggerui_blueprint)
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)