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
    Cria objeto Aluno apos validacoes.

    Parametros:
      nome: String do nome do aluno
      rm: Inteiro do RM (registro matricula)
      curso: String do curso
      mensalidade: Float do valor mensal

    Retorna: Objeto Aluno instanciado, ou None se algum dado invalido.

    Nota (v1.4.4): Melhor lancar ValueError em vez de retornar None
                   para controller saber exatamente qual campo falhou.
    """
    if not all([validar_nome(nome), validar_rm(rm), validar_curso(curso), validar_mensalidade(mensalidade)]):
        return None
    return Aluno(nome, rm, curso, mensalidade)

def validar_nome(nome: str) -> bool:
    """
    Valida se nome e string nao vazia.

    Parametro: nome - String ja coletada pela View
    Retorna: True se valido, False caso contrario

    Bug conhecido (v1.4.3):
      Linha atual usa `isinstance(nome, str) is None` que SEMPRE retorna False
      porque isinstance retorna True/False, nunca None.
      Validador sempre retorna True (aceita qualquer coisa!).

    Correcao necessaria (v1.4.4):
      if isinstance(nome, str) and nome.strip() != "":
          return True
      return False
    """
    if isinstance(nome, str) is False:
        return False
    return True

def validar_rm(rm: int) -> bool:
    """
    Valida se RM e inteiro positivo com maximo 6 digitos.

    Parametro: rm - Inteiro ja convertido pela View
    Retorna: True se valido, False caso contrario

    Bug conhecido (v1.4.3): Mesma logica errada do validar_nome (isinstance is None).

    Correcao necessaria (v1.4.4):
      - Checar se int e positivo: rm > 0
      - Checar max digitos: len(str(rm)) <= 6
      - Checar se RM ja existe (buscar no Repository)
    """
    if isinstance(rm,int) is None:
        return False
    return True

def validar_curso(curso: str) -> bool:
    """
    Valida se curso e string nao vazia.

    Parametro: curso - String ja coletada pela View
    Retorna: True se valido, False caso contrario

    Bug conhecido (v1.4.3): Mesma logica errada (isinstance is None).
    """
    if  isinstance(curso,str) is None:
        return False
    return True

def validar_mensalidade(valor: float) -> bool:
    """
    Valida se mensalidade e numero nao negativo.

    Parametro: valor - Float ja convertido pela View
    Retorna: True se valido, False caso contrario

    Bug conhecido (v1.4.3): Mesma logica errada (isinstance is None).

    Correcao necessaria (v1.4.4):
      if isinstance(valor, (int, float)) and valor >= 0:
          return True
      return False
    """
    if isinstance(valor, float) is None:
        return False
    return True
