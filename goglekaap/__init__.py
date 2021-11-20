from flask import (
    Flask,
    render_template,
    g
)

from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

csrf = CSRFProtect()
db = SQLAlchemy()
migrate = Migrate()

def create_app( config = None ):
    app = Flask( __name__ )
    app.logger.info( 'RUN Flask' )

    """Flask Configs"""
    from goglekaap.configs import DevelopmentConfig, ProductionConfig
    if not config:
        if app.config['DEBUG']:
            config = DevelopmentConfig()
        else:
            config = ProductionConfig()
    print( 'run with', config )
    app.config.from_object( config )

    """ CSRF INIT"""
    csrf.init_app( app )

    """ DB INIT """
    db.init_app( app )
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith( 'sqlite' ):
        migrate.init_app( app, db, render_as_batch = True )
    else:
        migrate.init_app( app, db )

    """ Routes INIT"""
    from goglekaap.routes import base_route, auth_route
    app.register_blueprint( base_route.bp )
    app.register_blueprint( auth_route.bp )

    """RESTX INIT"""
    from goglekaap.apis import blueprint as api
    app.register_blueprint( api )

    @app.errorhandler( 404 )
    def page_404( error ):
        # 리턴은 어떤 페이지로 render 할지, 에러 코드
        return render_template( '/404.html' ), 404

    @app.before_request
    def before_request():
        g.db = db.session

    @app.teardown_request
    def teardown_request( exception ):
        if hasattr( g, 'db' ):
            g.db.close()

    return app
