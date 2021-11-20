from goglekaap.configs import TestingConfig
from goglekaap import create_app
import pytest
import sys

# goglekaap을 가져오기 위해선 현재 디렉토리 경로를 path에 추가해야 한다.

sys.path.append('.')

@pytest.fixture
def client():
    app = create_app(TestingConfig())

    with app.test_client() as client:
        yield client

def test_auth(client):
    res = client.get(
        '/auth/register',
        # 만약 요청의 결과가 redirect이면 redirect된 최종 결과 값을 호출 302 X
        follow_redirects = True
    )
    print(res.status)
    assert res.status_code == 200
