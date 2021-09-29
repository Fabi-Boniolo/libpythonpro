from libpythonpro.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Fabiana', email='fabianaboniolo@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)



def test_listar_usuario(sessao):
    usuarios = [Usuario(nome='Fabiana', email = 'fabianaboniolo@gmail.com'),
                Usuario(nome='Renzo', email='fabianaboniolo@gmail.com')
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
