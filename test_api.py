from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_empresa():
    response = client.post("/empresas/", json={
        "nome": "Empresa Teste",
        "cnpj": "12345678901234",
        "endereco": "Rua Teste, 123",
        "email": "teste@empresa.com",
        "telefone": "81999999999"
    })
    assert response.status_code == 200
    assert response.json()["nome"] == "Empresa Teste"


def test_get_empresas():
    response = client.get("/empresas/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
