
from service.upload import *
from ._index import *
from werkzeug.datastructures import FileStorage
up_ns = Namespace('上传模块', description='上传相关操作')

upload_parser = up_ns.parser()
upload_parser.add_argument(
    'file',
    type=FileStorage,
    required=True,
    location='files',
    help='请选择要上传的文件'
)
upload_parser.add_argument(
    'type',
    type=str,
    required=True,
    help='请选择上传类型'
)


del_request = up_ns.model('删除操作', {
    'file_path': fields.String(required=True, description='文件路径')
})



def delete_handle():
    file_path = request.json.get('file_path')
    # 去掉前面的域名或者ip地址部分，只要相对于根目录的相对路径
    file_path = file_path.split('uploads/')[-1]
    return delete(file_path)

@up_ns.route('/upload')
class Upload(Resource):
    
    @up_ns.expect(upload_parser)
    def post(self):
        '''上传文件'''
        args = upload_parser.parse_args()
        file = args.get('file')
        t = args.get('type')
        if file is None:
            return file_error()
        return upload(file,t)
    @up_ns.expect(del_request)
    def delete(self):
        '''删除文件'''
        return delete_handle()
    