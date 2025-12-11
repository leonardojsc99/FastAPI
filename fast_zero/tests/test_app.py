from http import HTTPStatus

from fastapi.testclient import TestClient

from src.fast_zero.app import app



def test_root_deve_retornar_ok_e_ola_mundo():
    """
    Esse é um teste de três etapas normalmente chamado de AAA
    A:Arrange
    Antes de fazemos testes de requisições em algum endpoint que criamos, precisamos primeiro passar de onde estamos pegando esse endpoint, ou seja, 
    de qual API é isso. No nosso caso, a fase de Arrange é passar o client e a instância fastAPI para onde ele vai simular requsições

    A:Act
    Aqui é onde executamos o que queremos testar, no nosso caso, executamos um get no app.

    A:Assert
    Aqui é onde vemos ou garantimos que o que testamos está funcionando como queremos/deveria
    """
    #Arrange
    client = TestClient(app)

    #Act
    response = client.get('/')

    #Assert
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}
