
def test_get_users(client):
    res = client.get(
        '/api/users',
        follow_redirects=True
    )
    assert len(res.json) == 1
    assert res.status_code == 200

def test_get_user(client, user_data):
    print(type(user_data))
    res = client.get(
        '/api/users/1',
        follow_redirects = True
    )
    assert res.status_code == 200
    print()
    print(type(res.json))
    print(res.json)
    assert res.json.get('user_id') == user_data.get('user_id')

def test_post_user(client, user_data):
    res = client.post(
        '/api/users',
        data=user_data
    )
    assert res.status_code == 409

    new_user_data = user_data.copy()
    new_user_data['user_id'] = 'test_user_02'

    res = client.post(
        '/api/users',
        data = new_user_data
    )

    assert res.status_code == 201
