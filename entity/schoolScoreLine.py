from ._index import *


class SchoolScoreLine(db.Model):
    """学校分数线

    id 	主键
    exam_id 	考试id
    line_name 	分数线名称
    sum_ 	总分
    sumD 	总分段次
    Yuwen 	语文线	
    YuwenD 	语文线段次
    Shuxue 	数学线
    ShuxueD 	数学线段次
    Yingyu 	英语线
    YingyuD 	英语线段次
    Wuli 	物理线
    WuliD 	物理线段次
    HuaXue 	化学线
    HuaXueD 	化学线段次
    Zhengzhi 	政治线
    ZhengzhiD 	政治线段次
    Lishi 	历史线
    LishiD 	历史线段次
    Shengwu 	生物线
    ShengwuD 	生物线段次
    Dili 	地理线
    DiliD 	地理线段次
    update_time 	更新时间
    create_time 	创建时间
    """
    __tablename__ = 'school_score_line'
    id = db.Column(db.Integer, primary_key=True)
    exam_id = db.Column(db.Integer)
    line_name = db.Column(db.String(64))
    sum_ = db.Column(db.Integer)
    sumD = db.Column(db.Integer)
    Yuwen = db.Column(db.Float)
    YuwenD = db.Column(db.Integer)
    Shuxue = db.Column(db.Float)
    ShuxueD = db.Column(db.Integer)
    Yingyu = db.Column(db.Float)
    YingyuD = db.Column(db.Integer)
    Wuli = db.Column(db.Float)
    WuliD = db.Column(db.Integer)
    HuaXue = db.Column(db.Float)
    HuaXueD = db.Column(db.Integer)
    Zhengzhi = db.Column(db.Float)
    ZhengzhiD = db.Column(db.Integer)
    Lishi = db.Column(db.Float)
    LishiD = db.Column(db.Integer)
    Shengwu = db.Column(db.Float)
    ShengwuD = db.Column(db.Integer)
    Dili = db.Column(db.Float)
    DiliD = db.Column(db.Integer)
    update_time = db.Column(db.DateTime, default=datetime.datetime)
    create_time = db.Column(db.DateTime, default=datetime.datetime)
    def __repr__(self):
        return '<SchoolScoreLine %r>' % self.id