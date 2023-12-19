from flask import Blueprint, url_for

from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')
#main은 별칭, url prefix는 라우팅 함수의 애너테이션 URL을 의미
#url_prefix ='/' 대신 url_prefix='/main'이라고 하면
#localhost:5000이 아니라 localhost:5000/main/이 된다.

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/')
def index():
    return redirect(url_for('question._list'))
