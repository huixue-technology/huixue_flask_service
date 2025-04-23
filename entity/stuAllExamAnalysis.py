from _index import *

class StuAllExamAnalysis(db.Model):
    """学生考试进线次数分析（建议导表）

    id 	主键
    student_id 	学号
    school_id 	学校id
    year 	学年
    AllExam 	该学年考试总次数
    Sum_ 	总分
    Yuwen 	语文
    Shuxue 	数学
    Wuli 	物理
    Zhengzhi 	政治
    Lishi 	历史
    Shengwu 	生物
    Dili 	地理
    Huaxue 	化学
    Shengwu 	生物
    create_time 	创建时间
    update_time 	更新时间
    """
    __tablename__ = 'stu_all_exam_analysis'
    id = db.Column(db.Integer, primary_key=True,increment=True)
    student_id = db.Column(db.Integer)
    year = db.Column(db.String(64))
    AllExam = db.Column(db.Integer)
    Sum_ = db.Column(db.Integer)
    Yuwen = db.Column(db.Integer)
    Shuxue = db.Column(db.Integer)
    Wuli = db.Column(db.Integer)
    Zhengzhi = db.Column(db.Integer)
    Lishi = db.Column(db.Integer)
    Shengwu = db.Column(db.Integer)
    Dili = db.Column(db.Integer)
    Huaxue = db.Column(db.Integer)
    Shengwu = db.Column(db.Integer)
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now)
    def __repr__(self):
        return '<StuAllExamAnalysis %r>' % self.id