from app import app

def test_home():
    response = app.test_client.get('/')
    response.status_code = 200

    assert response.status_code == 200
    assert response.data == b"Hello world!"