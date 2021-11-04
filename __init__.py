# 하나의 디렉토리가 모듈화 된다.
import re
from flask import Flask

def create_app():
    print('run:' 'create_app()')
    app = Flask(__name__)

    @app.route('/')
    def indext():
        app.logger.info('RUN HELLO WORLD')
        return 'hello world'

    # 리퀘스트 훅  예제
    ''' Request Hook '''
    @app.before_request
    def before_request():
        app.logger.info('BEFORE_REQUEST')

    @app.before_first_request
    def before_first_request():
        app.logger.info('BEFORE_FIRST_REQUEST')
    
    @app.after_request
    def after_request(response):
        app.logger.info('AFTER REQEUST')
        # after request는 response를 리턴해야 함
        return response
    
    # teardown은 Reqeust가 끝날 때 실행된다.
    @app.teardown_request
    def teardown_request(exception):
        app.logger.info('TEARDOWN_REQUEST')

    
    return app