from flask import Blueprint, request, json
from service.user import *
from ._index import *

user_route = Blueprint('auth', __name__)

@user_route.route('/login', methods=['POST'])
# @swagger
def login_():
    """
    用户登录
    ---
    tags:
        - 用户管理
    summary: 用户登录接口
    description: 通过邮箱和密码进行用户登录
    parameters:
        - in: body
          name: body
          required: true
          description: 用户登录信息
          schema:
            type: object
            properties:
              email:
                type: string
                description: 用户邮箱
              password:
                type: string
                description: 用户密码
            example:
              email: example@example.com
              password: password123
    responses:
        200:
            description: 登录成功
            schema:
                type: object
                properties:
                    message:
                        type: string
                        description: 成功信息
                    token:
                        type: string
                        description: 用户认证令牌
    """
    data = request.json.get('data')
    if not data or not data['email'] or not data['password']:
        return not_found()
    return login(email=data['email'], password=data['password'])

@user_route.route('/bind_status')
# @swagger
def bind_status_():
    """
    身份绑定
    ---
    tags:
        - 用户管理
    summary: 获取身份绑定状态
    description: 获取当前用户的身份绑定状态
    responses:
        200:
            description: 返回身份绑定状态
            schema:
                type: string
    """
    return 'bind_status'

@user_route.route('/register', methods=['POST'])
# @swagger
def register_():
    """
    用户注册
    ---
    tags:
        - 用户管理
    summary: 用户注册接口
    description: 通过邮箱和密码进行用户注册
    parameters:
        - in: body
          name: body
          required: true
          description: 用户注册信息
          schema:
            type: object
            properties:
              email:
                type: string
                description: 用户邮箱
              password:
                type: string
                description: 用户密码
            example:
              email: example@example.com
              password: password123
    responses:
        200:
            description: 注册成功
            schema:
                type: object
                properties:
                    message:
                        type: string
                        description: 成功信息
    """
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
# @swagger
def modify_user_():
    """
    修改用户信息
    ---
    tags:
        - 用户管理
    summary: 修改用户信息接口
    description: 修改当前用户的信息
    responses:
        200:
            description: 修改成功
            schema:
                type: string
    """
    return 'modify_user'