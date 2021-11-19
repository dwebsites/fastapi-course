from app import schemas
from .database import client, session


def test_read_main(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_create_user(client):
    res = client.post(
        "/users/", json={"email": "hello1234@gmail.com", "password": "123"}
    )
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "hello1234@gmail.com"
    assert res.status_code == 201


def test_login_user(client):
    res = client.post(
        "/login", data={"username": "hello1234@gmail.com", "password": "123"}
    )
    print(res.json())
    assert res.status_code == 200
