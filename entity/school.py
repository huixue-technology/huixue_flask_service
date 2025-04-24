from ._index import *

class School(db.Model):
    """学校表->
        id:主键
        name:学校名称
        update_time:更新时间
        create_time:创建时间
    """
    __tablename__ = 'school'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    update_time = db.Column(db.DateTime, default=datetime.datetime)
    create_time = db.Column(db.DateTime, default=datetime.datetime)
    def __repr__(self):
        return '<School %r>' % self.name