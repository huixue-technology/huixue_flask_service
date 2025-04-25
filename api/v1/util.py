from flask import Blueprint,request
from service.util import send_code
from ._index import *
util_route = Blueprint('util', __name__)

@util_route.route('/send_code',methods=['GET'])
def send_code_():
    phone = request.args.get('phone')
    return send_code(phone)