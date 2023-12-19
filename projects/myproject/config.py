import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR,'pybo.db'))
#SQLALCHEMY_DATABASE_URI 접속 주소, SQlite 데이터베이스 사용 홈 디렉토리에 pybo.db로 저장
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "dev"
#SQLALCHEMY_TRACK_MODIFICATIONS 이벤트 처리 옵션
