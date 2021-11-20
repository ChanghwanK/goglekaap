import logging


def test_auth(client):
    res = client.get(
        '/auth/register',
        # 만약 요청의 결과가 redirect이면 redirect된 최종 결과 값을 호출 302 X
        follow_redirects = True
    )
    print(res.status)
    assert res.status_code == 200

    res = client.get(
        'auth/login',
        follow_redirects=True
    )
    assert res.status_code == 200

    res = client.get(
        'auth/logout',
        follow_redirects=True
    )
    assert res.status_code == 200

def test_base(client):
    res = client.get(
        '/',
        follow_redirects = True
    )
    print('hello')
    logging.info(res.status)
    assert res.status_code == 200
