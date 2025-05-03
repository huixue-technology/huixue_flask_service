from ._index import *

def add_scoreD(data):
    try:
        db.session.add(data)
        db.session.commit()
        return True
    except Exception as e:
        return e

def del_scoreD(score_id):
    try:
        print(score_id)
        ScoreD.query.filter(ScoreD.id == score_id.get('id')).delete()
        db.session.commit()
        return True
    except Exception as e:
        return e
    
def update_scoreD(data:ScoreD):
    try:
        print(data.to_dict())
        ScoreD.query.update(data.to_dict())
        db.session.commit()
        return True
    except Exception as e:
        return e
    
def get_scoreD(filter:dict,page:int = None,size:int = None):
    try:
        res = ScoreD.query
        if filter != None:
            res = res.filter_by(**filter) # 动态传递过滤条件
        res = res.paginate(page=page,per_page=size).items
        r = []
        print(res)
        for i in res: # 遍历结果
            r.append(i.to_dict())
        return r
    except Exception as e:
       return e