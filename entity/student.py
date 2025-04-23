from _index import *

class Student(db.Model):
    """学生表->
        id: 主键
        uid: 学号
        name: 学生真实姓名
        school_id: 所属学校
        grade: xx届
        class_id: 所属班级
        subject_selection_id: 所属选科
        state : 状态是否在读
        create_time: 创建时间
        update_time: 更新时间
    """
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(64))
    name = db.Column(db.String(64))
    school_id = db.Column(db.Integer)
    grade = db.Column(db.String(64))
    class_id = db.Column(db.Integer)
    '''选科表id：[{政史地:0},{物化生:1},{政史生:2}]'''
    subject_selection_id = db.Column(db.Integer)
    state = db.Column(db.Boolean)
    create_time = db.Column(db.DateTime, default=datetime.now) 
    update_time =db.Column(db.DateTime, default=datetime.now)
    def __repr__(self):
        return '<Student %r>' % self.name