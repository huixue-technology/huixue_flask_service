import json

def not_found():
    return json.dumps({"code": 404, "msg": "not found"})

def internal_server_error(e):
    return json.dumps({"code": 500, "msg": "internal server error","detail":str(e) if e else None})

def unauthorized():
    return json.dumps({"code": 401, "msg": "unauthorized"})

def bad_request():
    return json.dumps({"code": 400, "msg": "bad request"})

def params_error():
    return json.dumps({"code": 400, "msg": "params error"})

def params_not_found(e):
    return json.dumps({"code": 400, "msg": "params not found","detail":str(e) if e else None})
def success(data:str):
    return json.dumps({"code": 200, "msg": "success","data":data if data else None})
def token_expired():
    return json.dumps({"code": 401, "msg": "token expired"})

def token_error():
    return json.dumps({"code": 401, "msg": "token error"})