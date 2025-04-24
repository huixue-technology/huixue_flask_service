from ._index import *


class AllStudentQuestionScore(db.Model):
    """学生题目得分

    id 主键
    student_id 学生id
    school_id 学校id
    year 年份
    student_grade 年级
    subject 考试科目
    exam_id 考试id
    class_id 考试班级
    exam_type 考试类型
    show 是否显示
    objective_qscores 客观题得分
    subjective_qscores 主观题得分
    question_scores 每个题目得分，json
    create_time 创建时间
    update_time 更新时间
    """
    __tablename__ = 'all_student_question_score'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer)
    school_id = db.Column(db.Integer)
    year = db.Column(db.String(64))
    student_grade = db.Column(db.String(64))
    subject = db.Column(db.String(64))
    exam_id = db.Column(db.Integer)
    class_id = db.Column(db.String(64))
    show = db.Column(db.Boolean)
    objective_qscores = db.Column(db.Integer)
    subjective_qscores = db.Column(db.Integer)
    question_scores = db.Column(db.String(256))
    def __repr__(self):
        return '<AllStudentQuestionScore %r>' % self.id