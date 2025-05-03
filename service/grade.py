from ._index import *
from entity.scoreD import ScoreD
from data.scoreD import add_scoreD,del_scoreD,get_scoreD,update_scoreD
def convertScoreD(data):
    return ScoreD(
        id = data.get('id'),
        class_id=data.get('class_id'),
        exam_id=data.get('exam_id'),
        school_id=data.get('school_id'),
        student_id=data.get('student_id'),
        sumD=data.get('sumD'),
        sumB=data.get('sumB'),
        sum_=data.get('sum_'),
        show=data.get('show')
    )

def addScore(data):
    socre_d = convertScoreD(data)
    r = add_scoreD(socre_d)
    if isinstance(r,Exception):
        return internal_server_error(r)
    return success("添加学生成绩成功！")

def deleteScore(score_id):
    r = del_scoreD(score_id)
    print(r)
    if isinstance(r,Exception):
        return internal_server_error(r)
    return success("删除学生成绩成功！")

def updateScore(data):
    socre_d = convertScoreD(data)
    print(socre_d)
    r = update_scoreD(socre_d)
    if isinstance(r,Exception):
        return internal_server_error(r)
    return success("更新学生成绩成功！")

def getScore(filters,page,size):
    r = get_scoreD(filters,page,size)
    if isinstance(r,Exception):
        return internal_server_error(r)
    res = json.dumps(r)
    return success(res)