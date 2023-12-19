from pybo import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)#글자수가 제한됬을 때 db.String 사용
    content = db.Column(db.Text(), nullable = False)#글자 수를 제한할 수 없는 텍스트 db.Text
    create_date = db.Column(db.DateTime(), nullable=False)# nullable 빈값 허용 여부

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    question = db.relationship('Question', backref=db.backref('answer_set'))
    content = db.Column(db.Text(), nullable=False)
    #backref는 여러 개의 답변이 달릴 수 있는데 역참조는 이 답변들을 참조할 수 있음.
    #파이썬 코드로 질문 데이터를 삭제할 때 연결된 답변 모두를 삭제하기 바란다면 다음처럼 db.backref 설정에 cascade='all, delete-orphan'를 추가해야 한다.
    create_date = db.Column(db.DateTime(), nullable=False)

