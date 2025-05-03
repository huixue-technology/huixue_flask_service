from ._index import *

class ScoreD(db.Model):
    """学生考试成绩表

    id 主键
    student_id 学生id
    school_id 学校id
    exam_id 考试id
    class_id 考试班级
    sum_ 总分
    sumB 总分班次
    sumD 总分段次
    show 是否显示
    """
    
    __tablename__ = 'score_d'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer)
    school_id = db.Column(db.Integer)
    exam_id = db.Column(db.Integer)
    class_id = db.Column(db.String(64))
    sum_ = db.Column(db.Integer)
    sumB = db.Column(db.Integer)
    sumD = db.Column(db.Integer)
    show = db.Column(db.Boolean)

    def to_dict(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'school_id': self.school_id,
            'exam_id': self.exam_id,
            'class_id': self.class_id,
            'sum_': self.sum_,
            'sumB': self.sumB,
            'sumD': self.sumD,
            'show': self.show
        }