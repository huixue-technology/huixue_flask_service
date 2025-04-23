from _index import *


class StudentMistakes(db.Model):
    """学生错题表
    id主键	
    student_id学号	
    school_id学校id	
    examPaper_id考试id	
 
    exam_paper_info试卷信息 ：json格式[{
        {question_score,题目分值},
        {answer,参考答案},
        {question_path,题目路径},
        {answer_path,参考答案路径},
        {type,题目类型},
        {knowledge_point,知识点id},
        {question_myscores,题目得分},
        {question_schoolscores,全校均分}
    },] 存json加快数据库读取速度,可以考虑把对象做成一张表，再保存对应id列表，太繁不建议
    """
    __tablename__ = 'student_mistakes'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer)
    school_id = db.Column(db.Integer)
    exam_paper_id = db.Column(db.Integer)
    exam_paper_info = db.Column(db.Text)