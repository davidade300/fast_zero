from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retorner_ok_e_ola_mundo():
    client: TestClient = TestClient(app)  # Arrange -> prepara o ambiente

    response = client.get('/')  # Act -> acao principal do teste

    assert (
        response.status_code == HTTPStatus.OK
    )  # Assert -> verifica se tudo ocorreu como esperado
    assert response.json() == {'message': 'hello world!'}  # Assert
