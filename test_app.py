import app

def test_app():
    web = app.app.test_client()

    rv = web.get("/")
    assert rv.status_code == 200
    assert rv.text == "Hello <b>World!</b>"

def test_missing_page():
    web = app.app.test_client()

    rv = web.get("/hello")
    assert rv.status_code == 404

