from ._index import *
from service.grade import *
from util.page import page_handle
grade_ns = Namespace('grade', description='成绩管理相关操作')


add_score_request = grade_ns.model('添加成绩',{
    'student_id': fields.Integer(required=True, description='学生id'),
    'school_id': fields.Integer(required=True, description='学校id'),
    'exam_id': fields.Integer(required=True, description='考试id'),
    'class_id': fields.Integer(required=True, description='考试班级'),
    'sum_': fields.Integer(required=True, description='总分'),
    'sumB': fields.Integer(required=True, description='总分班次'),
    'sumD': fields.Integer(required=True, description='总分段次'),
    'show': fields.Boolean(required=False, description='是否显示'),
})

update_score_request = grade_ns.model('添加成绩',{
    'id': fields.Integer(required=False, description='成绩id'),
    'student_id': fields.Integer(required=False, description='学生id'),
    'school_id': fields.Integer(required=False, description='学校id'),
    'exam_id': fields.Integer(required=False, description='考试id'),
    'class_id': fields.Integer(required=False, description='考试班级'),
    'sum_': fields.Integer(required=False, description='总分'),
    'sumB': fields.Integer(required=False, description='总分班次'),
    'sumD': fields.Integer(required=False, description='总分段次'),
    'show': fields.Boolean(required=False, description='是否显示'),
})

del_score_request = grade_ns.model('删除成绩',{
    'id': fields.Integer(required=True, description='成绩id'),
})

get_score_request = grade_ns.parser()
get_score_request.add_argument('filter', type=str, required=False, help='过滤条件')
get_score_request.add_argument('page', type=int, required=False, help='页码')
get_score_request.add_argument('size', type=int, required=False, help='每页数量')

@grade_ns.route('')
class Grade(Resource):
    @grade_ns.expect(add_score_request)
    def post(self):
        '''添加学生成绩'''
        data = request.json
        addScore(data)
    
    @grade_ns.expect(del_score_request)
    def delete(self):
        '''删除学生成绩'''
        score_id = request.json
        return deleteScore(score_id)

    @grade_ns.expect(update_score_request)
    def put(self):
        '''修改学生成绩'''
        data = request.json
        return updateScore(data)

    @grade_ns.expect(get_score_request)
    def get(self):
        '''获取学生成绩(支持过滤条件)'''
        try:
            f,p,s = page_handle(request)
        except Exception as e:
            print(e)
            return params_error()
        return getScore(f,p,s)