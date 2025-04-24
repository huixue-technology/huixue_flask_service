from ._index import *

class ExamPaper(db.Model):
    """试卷信息
    
    id 试卷id
    exam_id 考试id
    subject 试卷科目
    question_info 试卷题目信息，用json存储[{
        {question_id:题号},
        {question_score:题目得分},
        {answer:参考答案},
        {question_path:题目路径},
        {answer_path:参考答案路径},
        {type:题型},
        {knowledge_point:知识点id}
    },]
    """
    __tablename__ = 'exam_paper'
    id = db.Column(db.Integer, primary_key=True)
    exam_id = db.Column(db.Integer)
    subject = db.Column(db.String(64))
    question_info = db.Column(db.Text)
    def __repr__(self):
        return '<ExamPaper %r>' % self.id