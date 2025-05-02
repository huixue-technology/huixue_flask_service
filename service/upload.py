import os
from ._index import *
def upload(file,t:str):
    try:
        # 先暂时存到项目中，到时候可以改到对应的服务器位置上
        file.save(f'uploads/{t}/{file.filename}')
    except Exception as e:
        return internal_server_error(e)
    return success(file.filename)


def delete(file_path:str):
    try:
        os.remove(f'uploads/{file_path}')
    except Exception as e:
        return internal_server_error(e)
    return success()