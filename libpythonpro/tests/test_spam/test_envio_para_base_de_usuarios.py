from unittest.mock import Mock

import pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
                Usuario(nome='Fabiana', email = 'fabianaboniolo@gmail.com'),
                Usuario(nome='Renzo', email='renzo@python.com')
       ],
       [
                Usuario(nome='Fabiana', email = 'fabianaboniolo@gmail.com'),

       ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'fabianaboniolo@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos '
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Fabiana', email = 'fabianaboniolo@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'renzo@python.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos '
    )
    enviador.enviar.assert_called_once_with (
        'renzo@python.com',
        'fabianaboniolo@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos '

    )