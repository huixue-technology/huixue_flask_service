from flask import Blueprint,request,json
from service.user import *
from ._index import *
user_route = Blueprint('auth', __name__)


@user_route.route('/login',methods=['POST'])
def login_():
    """user用戶登录"""
    data = request.json.get('data')
    if not data or not data['email'] or not data['password']: 
        return not_found()
    return login(email = data['email'],password = data['password'])
@user_route.route('/bind_status')
def bind_status_():
    """身份绑定"""
    return 'bind_status'

@user_route.route('/register',methods=['POST'])
def register_():
    """用户注册"""
    data = request.json['data']
    
    print(data.get('email'))
    if not data: 
        return params_error()
    elif not data.get('email'):
        return params_not_found('email')
    elif not data.get('password'):
        return params_not_found('password')
    return register(data)

@user_route.route('/modify_user')
def modify_user_():
    """修改用户信息"""
    return 'modify_user'
