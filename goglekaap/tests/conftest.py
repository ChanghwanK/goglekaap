from goglekaap.configs import TestingConfig
from goglekaap import create_app, db
from goglekaap.model.user import User
import pytest
import sys

# goglekaap을 가져오기 위해선 현재 디렉토리 경로를 path에 추가해야 한다.

sys.path.append('.')

@pytest.fixture(scope = 'session')
def user_data():
    yield dict(
        user_id = 'test_user_id',
        user_name = 'test_user_name',
        password = 'test_password'
    )

    # yield User('test', 'user_name', 'password')

@pytest.fixture(scope = 'session')
def app(user_data):
    app = create_app(TestingConfig())

    with app.app_context():
        db.drop_all()
        db.create_all()
        db.session.add(User(**user_data))
        db.session.commit()
    yield app

@pytest.fixture(scope = 'session')
def client(app):
    with app.test_client() as client:
        yield client

