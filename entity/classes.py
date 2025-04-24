from ._index import *


class Classes(db.Model):
    """班级表——>
        id:主键
        name:班级名称
        header_id:班主任id
        school_id:学校id
        create_time:创建时间
        update_time:更新时间
    """
    __tablename__ = 'classes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    header_id = db.Column(db.Integer) 
    school_id = db.Column(db.Integer)
    create_time = db.Column(db.DateTime, default=datetime.datetime)
    update_time = db.Column(db.DateTime, default=datetime.datetime)
    def __repr__(self):
        return '<Classes %r>' % self.name