from _index import  *

class Exam(db.Model):
    """考试id-名对应表
        id - 名称，也可自定义但不可重复
        name - 名称，可重复
        year - 考试的学年，xx年
        student_grade - 考试年级，xx届
        exam_type 考试类型：目前只有2种，1代表高三的文理科，2代表高一、高二的选科
        exam_paper_ids - 考试试卷id，以逗号分隔[,]
        update_time - 更新时间
        create_time - 创建时间
    """
    
    __tablename__ = 'exam'
    id = db.Column(db.Integer,unique=True,increment=True,primary_key=True)
    name = db.Column(db.String(64))
    year = db.Column(db.String(64))
    student_grade = db.Column(db.String(64))
    exam_type = db.Column(db.String(64))
    exam_paper_ids = db.Column(db.String(256))
    update_time = db.Column(db.DateTime,default=datetime.now)
    create_time = db.Column(db.DateTime,default=datetime.now)