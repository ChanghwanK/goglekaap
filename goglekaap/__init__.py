# 하나의 디렉토리가 모듈화 된다.
from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

csrf = CSRFProtect()
db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.logger.info('RUN Flask')

    """
     SECRET KEY
     WTF를 사용하기 위해선 SECRET KEY가 무조건 등록이 되어있어야 한다.
     이유는 CSRF Token이 암호화 되어있기 때문에 
    """
    app.config['SECRET_KEY'] = 'secret key'
    app.config['SESSION_COOKIE_NAME'] = 'goglekaap'

    """ 
    DB Config
    """
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost:3308/goglekaap?charset=utf8'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    """ Static Cache Time Change """
    # static file Cache time (max-age)을 1초로 변경 기본은 12시간
    # DEBUG MODE 때는 이를 1초로 한다.
    if app.config['DEBUG']:
        app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

    """ DB INIT """
    db.init_app(app)

    if app.config['SQLALCHEMY_DATABASE_URI'].startswith('sqlite'):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)

    """ Routes INIT"""
    from goglekaap.routes import base_route, auth_route
    app.register_blueprint(base_route.bp)
    app.register_blueprint(auth_route.bp)

    """ CSRF INIT"""
    csrf.init_app(app)

    @app.errorhandler(404)
    def page_404(error):
        # 리턴은 어떤 페이지로 render 할지, 에러 코드
        return render_template('/404.html'), 404

    return app
