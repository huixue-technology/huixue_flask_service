from ._index import *


class ClassGradeAnalysis(db.Model):
    """班级年级分析

    name 考试名称，xx月考
    exam_id 考试id
    Sum 总分一本过线人数
    Yuwen 语文一本过线人数
    Shuxue 数学一本过线人数
    Zhengzhi 政治一本过线人数
    Lishi 历史一本过线人数
    Dili 地理一本过线人数
    Wuli 物理一本过线人数
    Huaxue化学一本过线人数
    Shengwu 生物一本过线人数
    create_time 创建时间
    update_time 更新时间
    """
    
    __tablename__ = 'class_grade_analysis'
    id = db.Column(db.Integer, primary_key=True)
    exam_id = db.Column(db.Integer)
    class_grade = db.Column(db.String(64))
    Sum = db.Column(db.Integer)
    Yuwen = db.Column(db.Integer)
    Shuxue = db.Column(db.Integer)
    Zhengzhi = db.Column(db.Integer)
    Lishi = db.Column(db.Integer)
    Dili = db.Column(db.Integer)
    Wuli = db.Column(db.Integer)
    Huaxue = db.Column(db.Integer)
    Shengwu = db.Column(db.Integer)
    create_time = db.Column(db.DateTime, default=datetime.datetime)
    update_time = db.Column(db.DateTime, default=datetime.datetime)
    def __repr__(self):
        return '<ClassGradeAnalysis %r>' % self.name