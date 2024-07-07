import app

def test_qqrq():
    web = app.app.test_client()

    rv = web.get("/")
    assert rv.status_code == 200

