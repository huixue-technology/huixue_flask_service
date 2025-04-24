from ._index import *

class Teacher(db.Model):
    """老师表->
        id 主键
        uid 工号
        name 姓名
        subject 科目
        school_id 学校id
        update_time 更新时间
        create_time 创建时间
    """
    
    __tablename__ = 'teacher'
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(64))
    name = db.Column(db.String(64))
    subject = db.Column(db.String(64))
    school_id = db.Column(db.Integer)
    update_time = db.Column(db.DateTime, default=datetime.datetime)
    create_time = db.Column(db.DateTime, default=datetime.datetime)
    def __repr__(self):
        return '<Teacher %r>' % self.name