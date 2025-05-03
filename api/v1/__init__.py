from flask_restx import Api
from .user import user_ns
from .upload import up_ns
from .grade import grade_ns

def init_restx():
    api = Api(
        title='慧学 API 接口文档',
        version='1.0',
        description='API 文档描述',
    )
    api.add_namespace(user_ns)
    api.add_namespace(grade_ns)
    api.add_namespace(up_ns)
    return api

api = init_restx()