from ._index import *

class ClassMistakes(db.Model):
    """班级错题

    id 主键
    school_id 学校id
    class_id 班级id
    exam_paper_id 试卷id
    exam_id 考试id
    subject 考试科目
    question_type 考试题型
    question_id 错题id
    question_score 题目分值
    answer 错题答案
    question_path 错题路径
    answer_path 错题答案路径
    knowledge_point_id 错题知识点id
    create_time 创建时间
    update_time 更新时间
    question_classcores 班级得分
    question_schoolscores 全校得分
    question_classerrorcount 班级错误人数
    question_classallcount 班级总人数
    question_classerrorname 错误名单[姓名：得分]json
    class_id 班级id
    """
    __tablename__ = 'class_mistakes'
    id = db.Column(db.Integer, primary_key=True)
    school_id = db.Column(db.Integer)
    class_id = db.Column(db.Integer)
    exam_paper_id = db.Column(db.Integer)
    exam_id = db.Column(db.Integer)
    subject = db.Column(db.String(64))
    question_type = db.Column(db.String(64))
    question_id = db.Column(db.Integer)
    question_score = db.Column(db.Integer)
    answer = db.Column(db.String(256))
    question_path = db.Column(db.String(256))
    answer_path = db.Column(db.String(256))
    knowledge_point_id = db.Column(db.String(64))
    question_classcores = db.Column(db.Integer)
    question_schoolscores = db.Column(db.Integer)
    question_classerrorcount = db.Column(db.Integer)
    question_classallcount = db.Column(db.Integer)
    question_classerrorname = db.Column(db.Text(2550))