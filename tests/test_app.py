from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient

from fast_zero.app import app


# fixture é como função que prepara dados ou estado necessários para o teste.
@pytest.fixture
def client():
    return TestClient(app)


def test_root_deve_retorner_ok_e_ola_mundo(client):
    # client: TestClient = TestClient(app)  # Arrange -> prepara o ambiente

    response = client.get('/')  # Act -> acao principal do teste

    # Assert -> verifica se tudo ocorreu como esperado
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'hello world!'}  # Assert


def test_exercicio_aula_2_retorna_html(client):
    # client: TestClient = TestClient(app)  # Arrange -> prepara o ambiente

    response = client.get('/teste-html')  # Act -> acao principal do teste

    assert response.status_code == HTTPStatus.OK
    assert '<h1>Olá Mundo</h1>' in response.text


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'alice',
        'email': 'alice@example.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'alice',
                'email': 'alice@example.com',
                'id': 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'bob',
        'email': 'bob@example.com',
        'id': 1,
    }


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'user deleted'}
