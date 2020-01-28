from usuario import Usuario
from faker import Faker

fake = Faker()

novo_usuario = Usuario(
       nome=fake.first_name(),
        sobrenome=fake.last_name(),
        trabalho=fake.job(),
        endereco=fake.address()
    )


def test_instance_of_user():
    assert isinstance(novo_usuario, Usuario)

def test_nome():
    nome_esperado = novo_usuario.nome
    assert nome_esperado == novo_usuario.nome, 'nome ok'


def test_sobrenome():
    sobrenome_esperado = novo_usuario.sobrenome
    assert sobrenome_esperado == novo_usuario.sobrenome, 'sobrenome ok'


def test_trabalho():
    trabalho_esperado = novo_usuario.trabalho
    assert trabalho_esperado == novo_usuario.trabalho, 'trabalho ok'


def test_endereco():
    endereco_esperado = novo_usuario.endereco
    assert endereco_esperado == novo_usuario.endereco, 'endereco ok'
