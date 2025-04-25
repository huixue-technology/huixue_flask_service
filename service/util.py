import random
from flask import session

def send_code(phone):
    code = random.randint(1000,9999)
    # 把验证码和手机号存到session中
    session[phone] = code
    return code