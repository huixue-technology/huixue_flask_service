from ._index import *

class KeyStuAnalysis(db.Model):
    """学生进线率分析

    id 主键
    student_id 学生id
    exam_id 考试id 新增
    subject 科目：0表示总的
    rate 进线率
    update_time 更新时间
    create_time 创建时间
    """

    __tablename__ = 'key_stu_analysis'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer)
    exam_id = db.Column(db.Integer)
    subject = db.Column(db.String(64))
    rate = db.Column(db.Float)
    update_time = db.Column(db.DateTime, default=datetime.datetime)
    create_time = db.Column(db.DateTime, default=datetime.datetime)