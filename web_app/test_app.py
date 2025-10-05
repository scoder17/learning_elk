import json
from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_add_success():
    client = app.test_client()
    response = client.post("/add", json={"a": 2, "b": 3})
    data = json.loads(response.data)
    assert data["result"] == 5

def test_add_failure():
    client = app.test_client()
    response = client.post("/add", json={})
    assert response.status_code == 400