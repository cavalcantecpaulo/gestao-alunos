from Codigos.models.aluno_model import Aluno
from Codigos.services.aluno_service import validar_nome, validar_rm, validar_curso, validar_mensalidade


def test_nome_encontrado():
    aluno = Aluno("Neymar", 1001, "Fisioterapia", 1200)

    assert aluno.nome == "Neymar"

def test_rm_encontrado():
    aluno = Aluno("João", 1002, "Música", 2000)

    assert aluno.rm == 1002

def test_curso_encontrado():
    aluno = Aluno("Allan", 1003, "Ciências Sociais", 700)

    assert aluno.curso == "Ciências Sociais"

def test_mensalidade_encontrada():
    aluno = Aluno("Rodrigo", 1004, "Administração", 1800)

    assert aluno.mensalidade == 1800

def test_validar_nome():
    nome = "Paulão"

    assert validar_nome(nome) is True

def test_validar_rm():
    rm = 123456

    assert validar_rm(rm) is True

def test_validar_curso():
    curso = "Engenharia de Software"

    assert validar_curso(curso) is True

def test_validar_mensalidade():
    mens = 1500.00

    assert validar_mensalidade(mens) is True

def test_validacao_nome_falha():
    nome = ""

    assert validar_nome(nome) is False

def test_validacao_rm_falha():
    rm = "2929s"

    assert validar_rm(rm) is False

def test_validacao_curso_falha():
    curso = ""

    assert validar_curso(curso) is False

def test_validacao_mensalidade_falha():
    mens = -22

    assert validar_mensalidade(mens) is False