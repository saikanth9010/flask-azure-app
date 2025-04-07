from app.main import app

def test_home():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b"Welcome" in response.data

def test_about():
    response = app.test_client().get('/about')
    assert response.status_code == 200
    assert b"About" in response.data
