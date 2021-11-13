# 하나의 디렉토리가 모듈화 된다.
from flask import Flask
from flask import render_template


def create_app():
    app = Flask(__name__)
    app.logger.info('RUN Flask')

    # static file Cache time (max-age)을 1초로 변경 기본은 12시간
    # DEBUG MODE 때는 이를 1초로 한다.
    if app.config['DEBUG']:
        app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

    @app.route('/')
    def index():
        app.logger.info('RUN Hello Flask')
        return render_template('index.html')

    @app.errorhandler(404)
    def page_404(error):
        # 리턴은 어떤 페이지로 render 할지, 에러 코드
        return render_template('/404.html'), 404

    return app

