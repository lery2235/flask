from flask import Flask

def create_app():
    app = Flask(__name__) # 애플리케이션 팩토리

    @app.route('/')
    def hello_pybo():
        return 'Hello, Pybo!'

    return app
