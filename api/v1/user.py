from flask import  request
from service.user import *
from ._index import *

user_ns = Namespace('user', description='用户相关操作')

login_request = user_ns.model('登录', {
    'email': fields.String(required=True, description='用户邮箱'),
    'password': fields.String(required=True, description='用户密码')
})

bind_request = user_ns.model('绑定', {
    'bind_id': fields.String(required=True, description='绑定id'),
    'id': fields.String(required=True, description='用户id')
})

register_request = user_ns.model('注册', {
    'name': fields.String(required=True, description='用户名'),
    'wxid': fields.String(required=False, description='微信id'),
    'role': fields.String(required=False, description='角色'),
    'school_id': fields.String(required=False, description='学校id'),
    'phone': fields.String(required=False, description='手机号'),
    'email': fields.String(required=True, description='邮箱'),
    'password': fields.String(required=True, description='密码'),
    'bind_state': fields.Boolean(required=False, description='绑定状态')
})

modify_request = user_ns.model('修改', {
    'name': fields.String(required=False, description='用户名'),
    'wxid': fields.String(required=False, description='微信id'),
    'role': fields.String(required=False, description='角色'),
    'school_id': fields.String(required=False, description='学校id'),
    'phone': fields.String(required=False, description='手机号'),
    'email': fields.String(required=False, description='邮箱'),
    'password': fields.String(required=False, description='密码'),
    'bind_state': fields.Boolean(required=False, description='绑定状态')
})

delete_request = user_ns.model('删除', {
    'id': fields.String(required=True, description='用户id')
})

get_request = user_ns.parser()
get_request.add_argument('filter',type=str,required=False,help='查询条件')
get_request.add_argument('page',type=int,required=False,help='页码')
get_request.add_argument('size',type=int,required=False,help='每页数量')

@user_ns.route('/login')
class Login(Resource):
    @user_ns.expect(login_request)
    def post(self):
        data = request.json.get('data')
        if not data or not data['email'] or not data['password']:
            return not_found()
        return login(email=data['email'], password=data['password'])



@user_ns.route('/bind_status')
class BindStatus(Resource):
    @user_ns.expect(bind_request)
    def post(self):
        '''用户绑定身份'''
        data = request.json
        return bind_status(data)


@user_ns.route('')
class User(Resource):
    @user_ns.expect(register_request)
    def post(self):
        '''用户注册'''
        data = request.json
        if not data.get('email'):
            return params_not_found('email')
        elif not data.get('password'):
            return params_not_found('password')
        return register(data)
    @user_ns.expect(modify_request)
    def put(self):
        '''修改用户'''
        data = request.json
        if not data:
            return params_error()
        return updateUser(data)
    @user_ns.expect(delete_request)
    def delete(self):
        '''删除用户'''
        data = request.json
        if not data:
            return params_error()
        return deleteUser(data)
    @user_ns.expect(get_request)
    def get(self):
        '''查询用户(支持过滤条件)'''
        try:
            filter_str = request.args.get('filter')  # 获取字符串形式的 JSON
            f = json.loads(filter_str) if filter_str else None
            p = request.args.get('page')
            s = request.args.get('size')
        except Exception as e:
            return params_error()
        return getUser(f,p,s)