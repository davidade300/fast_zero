from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retorner_ok_e_ola_mundo():
    client: TestClient = TestClient(app)  # Arrange -> prepara o ambiente

    response = client.get('/')  # Act -> acao principal do teste

    # Assert -> verifica se tudo ocorreu como esperado
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'hello world!'}  # Assert


def test_exercicio_aula_2_retorna_html():
    client: TestClient = TestClient(app)  # Arrange -> prepara o ambiente

    response = client.get('/teste-html')  # Act -> acao principal do teste

    assert response.status_code == HTTPStatus.OK
    assert '<h1>Olá Mundo</h1>' in response.text
