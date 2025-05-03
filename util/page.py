
from ._index import *


def page_handle(request):
    filter_str = request.args.get('filter')
    p = request.args.get('page')
    s = request.args.get('size')
    if filter_str:
        filter_str = json.loads(filter_str)
    return filter_str,p,s