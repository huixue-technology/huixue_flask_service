
from ._index import *


def add_user(user:User):
    try:
        db.session.add(user)
        db.session.commit()
        return True
    except Exception as e:
        return e
    
def del_user(user:User):
    try:
        db.session.delete(user)
        db.session.commit()
        return True
    except Exception as e:
        return e
def get_user(filter:dict,page:int = None,size:int = None):
    try:
        res = User.query
        if filter != None:
            res = res.filter_by(**filter) # 动态传递过滤条件
        res = res.paginate(page=page,per_page=size).items
        r = []
        for i in res: # 遍历结果
            r.append(i.to_dict())
        return r
    except Exception as e:
        return e
    
def update_user(user:User):
    try:
        db.session.update(user)
        db.session.commit()
        return True
    except Exception as e:
        return e