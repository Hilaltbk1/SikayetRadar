from fastapi.testclient import TestClient
from sqlalchemy.orm import session

from database import get_session
from routers.main import app  # Uygulama örneğini içe aktarın

client = TestClient(app)


def test_create_user():
    def get_session_override():
        return session

    app.dependency_overrides[get_session] = get_session_override
    response = client.post(
        "/users/", json={"name": "hilal", "username": "hilaltabak", "password": "hilal123"}
    )
    data = response.json()

    # API'nin yanıt kodunu kontrol et
    assert response.status_code == 201  # Daha yaygın olan yanıt kodu

    # API'nin döndürdüğü veri ile karşılaştırma yap
    assert data["name"] == "hilal"
    assert data["username"] == "hilaltabak"
    assert data["password"] == "hilal123"