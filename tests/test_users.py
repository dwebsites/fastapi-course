from inspect import cleandoc
import pytest
from starlette.responses import Response
from app import schemas
from jose import jwt
from app.config import settings



# def test_read_main(client):
#     response = client.get("/")
#     assert response.status_code == 200
#     assert response.json() == {"message": "Hello World"}


# def test_create_user(client):
#     res = client.post(
#         "/users/", json={"email": test_user['email'], "password": test_user['password']}
#     )
#     new_user = schemas.UserOut(**res.json())
#     assert new_user.email == "test@gmail.com"
#     assert res.status_code == 201


def test_login_user(client, test_user):
    res = client.post(
        "/login", data={"username": test_user['email'], "password": test_user['password']}
    )
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms=[settings.algorithm])
    id = payload.get("user_id")
    print(res.json())
    assert id == test_user["id"]
    assert login_res.token_type == 'bearer'
    assert res.status_code == 200

@pytest.mark.parametrize("email, password, status_code", [
        ('wrongemail@gmail.com', 'password123', 403),
    ('sanjeev@gmail.com', 'wrongpassword', 403),
    ('wrongemail@gmail.com', 'wrongpassword', 403),
    (None, 'password123', 422),
    ('sanjeev@gmail.com', None, 422)
])
def test_incorect_login(test_user, client, email, password, status_code):
    res = client.post("/login", data={"username": email, "password": password})

    assert res.status_code == status_code