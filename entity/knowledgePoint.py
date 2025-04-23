from _index import *


class KnowledgePoint(db.Model):
    """知识点

    id 主键
    code_id 知识点编码
    subject 科目
    hierarchy 层级
    description 描述
    """
    __tablename__ = 'knowledge_point'
    id = db.Column(db.Integer, primary_key=True)
    code_id = db.Column(db.String(64))
    subject = db.Column(db.String(64))
    hierarchy = db.Column(db.String(64))
    description = db.Column(db.Text)