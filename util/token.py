import jwt
from datetime import datetime, timezone,timedelta
from jwt import PyJWTError
from flask import current_app
from .reponse import token_expired,token_error
JWT_TOKEN_EXPIRE_TIME = 24  # token有效时间 24小时
JWT_SECRET = 'abc'   # 加解密密钥
JWT_ALGORITHM = 'HS256'  # 加解密算法

def generate_tokens(email:str,id):
	'''生成token
	
	'''
	playload={
		'id':id,
		'email':email,
		'exp':datetime.now(timezone.utc)+timedelta(hours=JWT_TOKEN_EXPIRE_TIME)
	}
	return jwt.encode(payload=playload,key=JWT_SECRET,algorithm=JWT_ALGORITHM)


def verify_token(token):
	'''验证token
	
	'''
	try:
		_payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
		exp = _payload.pop('exp')
		if datetime.fromtimestamp(exp) < datetime.now(timezone.utc): 
			return token_expired()
		else:
			return True
	except PyJWTError as e:
		return token_error()
    