"""
Service de Aluno: Contem logica pura de validacao e criacao de objetos.

Responsabilidades:
  - Validar dados ja coletados (recebe str/int/float, retorna bool)
  - Criar objetos Aluno a partir de dados validados
  - Definir regras de negocio (ex: RM maximo 6 digitos, mensalidade >= 0)

O que NAO faz:
  - input() ou print() (isso e responsabilidade da View)
  - Persistir dados (isso e responsabilidade do Repository)
  - Saber onde dados vem ou vao (independencia de I/O)

Beneficio: Funcoes sao "puras" e testaveis isoladamente.
  Exemplo: validar_nome("Joao") retorna True sem precisar digitar no terminal!
"""

from Codigos.models.aluno_model import Aluno
from Codigos.views.aluno_view import validacao_nome, validacao_rm, validacao_curso, validacao_mensalidade

def criar_objeto_aluno(nome, rm, curso, mensalidade) -> Aluno | None:
    """
    Cria objeto Aluno após validações.

    Parametros:
      nome: String do nome do aluno
      rm: Inteiro do RM (registro matricula)
      curso: String do curso
      mensalidade: Float do valor mensal

    Retorna: Objeto Aluno instanciado, ou None se algum dado invalido.

    """
    try:
        if not all([validar_nome(nome), validar_rm(rm), validar_curso(curso), validar_mensalidade(mensalidade)]):
            return Aluno(nome, rm, curso, mensalidade)
    except ValueError:
        print("Erro ao criar objeto Aluno: dados inválidos!!!")

def validar_nome(nome: str) -> bool:
    """
    Valida se nome e string nao vazia.

    Parametro: nome - String ja coletada pela View
    Retorna: True se valido, False caso contrario

    """
    if not isinstance(nome, str) or nome == "":
        return False
    return True

def validar_rm(rm: int) -> bool:
    """
    Valida se RM e inteiro positivo com maximo 6 digitos.

    Parametro: rm - Inteiro ja convertido pela View
    Retorna: True se valido, False caso contrario

    Correcao necessaria (v1.4.4):
      - Checar se int e positivo: rm > 0
      - Checar max digitos: len(str(rm)) <= 6
      - Checar se RM ja existe (buscar no Repository)
    """
    if not isinstance(rm,int):
        return False
    return True

def validar_curso(curso: str) -> bool:
    """
    Valida se curso e string nao vazia.

    Parametro: curso - String ja coletada pela View
    Retorna: True se valido, False caso contrario
    """
    if not isinstance(curso,str) or curso == "":
        return False
    return True

def validar_mensalidade(valor: float) -> bool:
    """
    Valida se mensalidade e numero nao negativo.

    Parametro: valor - Float ja convertido pela View

    Correcao necessaria (v1.4.4):
      if isinstance(valor, (int, float)) and valor >= 0:
          return True
      return False
    """
    if not isinstance(valor, float):
        return False
    return True
