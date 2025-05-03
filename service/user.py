
from entity.user import User
from data.user import add_user,get_user,update_user,del_user
from ._index import *
def convertUser(data):
    user = User(
        name = data.get('name'),
        phone = data.get('phone'),
        password = data.get('password'),
        wxid = data.get('wxid'),
        school_id = data.get('school_id'),
        role = data.get('role'),
        email = data.get('email'),
        bind_state = data.get('bind_state') if data.get('bind_state') else False,
        update_time = datetime.now(),
        create_time = datetime.now(),
    )
    return user
def login(email:str,password:str):
    res = get_user({'email':email,'password':password})
    if isinstance(res, Exception):
        return internal_server_error(res)
    elif res == None:
        return unauthorized()
    token  = generate_tokens(email,res[0].id)
    return success(token)

def register(data):
    user = convertUser(data)
    res = add_user(user)
    if res:
        return success(str(res))
    return internal_server_error(res)

def deleteUser(data):
    id = data.get('id')
    if id == None:
        return params_not_found('id')
    res = del_user(id)
    if res == True:
        return success("删除用户成功！")
    return internal_server_error(res)

def updateUser(data):
    user = convertUser(data)
    res = update_user(user)
    if res == True:
        return success("修改用户成功！")
    return internal_server_error(res)

def getUser(filter,page,size):
    res = get_user(filter,page,size)
    if isinstance(res, Exception):
        return internal_server_error(res)
    r = json.dumps(res)
    return success(r)

def bind_status(data):
    bind_id = data.get('bind_id')
    if bind_id == None:
        return params_not_found('bind_id')
    user_id = data.get('id')
    res = update_user(User(id=user_id,bind_state=bind_id))
    if isinstance(res, Exception):
        return internal_server_error(res)
    elif res == None:
        return params_not_found(data)
    return success()