from ._index import *

class User(db.Model):
    """用户表：需要绑定角色身份—>
    id: 用户id
    name: 用户名
    wxid: 微信id
    role: 角色
    school_id: 学校id
    phone: 手机号
    email: 邮箱
    password: 密码
    bind_state: 看这个用户是否绑定了学生
    update_time: 更新时间
    create_time: 创建时间
    """
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    wxid = db.Column(db.String(64), unique=True)
    role = db.Column(db.String(64)) # enumerate(['admin','teacher','student','parent'])
    school_id = db.Column(db.Integer)
    phone = db.Column(db.String(64))
    email = db.Column(db.String(64))
    password = db.Column(db.String(64))
    bind_state = db.Column(db.Boolean, default=False)
    update_time = db.Column(db.DateTime, default=datetime.datetime)
    create_time = db.Column(db.DateTime, default=datetime.datetime)
    def __repr__(self):
        return '<User %r>' % self.name