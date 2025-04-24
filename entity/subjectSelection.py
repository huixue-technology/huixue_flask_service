from ._index import *

class SubjectSelection(db.Model):
    """选科对应id
    
    政史地物化生六选三组合成对应id
    政史地 0 
    政史生 1
    政史物 2
    政史化 3
    政物地 4
    政物生 6
    政物化 7
    政化地 8
    政化生 9
    政生地 10
    史地生 11
    史地物 12
    史地化 13
    史物生 14
    史物化 15
    生地物 16
    生地化 17
    生物化 18
    地生化 19
    地物化 20
    """
    
    __tablename__ = 'subject_selection'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    create_time = db.Column(db.DateTime, default=datetime.datetime)
    update_time = db.Column(db.DateTime, default=datetime.datetime)
    def __repr__(self):
        return '<SubjectSelection %r>' % self.name