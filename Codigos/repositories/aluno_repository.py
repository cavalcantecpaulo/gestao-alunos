"""
Repository de Aluno: Gerencia acesso a dados (em memoria e JSON).

Responsabilidades:
  - Gerenciar lista_alunos (memoria temporaria)
  - Buscar alunos por RM
  - Salvar lista completa em JSON
  - (Futuro v1.4.4) Adicionar/atualizar/remover individual
  - (Futuro v1.4.5) Carregar JSON ao iniciar

O que NAO faz:
  - Validar dados (responsabilidade do Service)
  - Coletar input do usuario (responsabilidade da View)
  - Exibir dados (responsabilidade da View)

Beneficio: Quando precisar trocar JSON por banco de dados,
           muda so este arquivo. Service e View nao sabem
           onde dados vivem.
"""

import json

lista_alunos = []

def busca_aluno_rm(rm: int) -> dict | None:
    """
    Busca aluno especifico pelo RM.

    Parametro: rm - Numero de registro matricula (inteiro)
    Retorna: Dicionario do aluno se encontrado, None se nao existir

    Uso tipico:
      aluno = busca_aluno_rm(123456)
      if aluno:
          print(aluno["nome_aluno"])
      else:
          print("Aluno nao encontrado")
    """
    for aluno in lista_alunos:
        if aluno["rm"] == rm:
            return aluno
    else:
        return None

def salvando_lista_json() -> None:
    """
    Salva lista completa de alunos em arquivo JSON.

    Arquivo: dados_alunos.json (raiz do projeto)
    Formato: Lista de dicionarios

    Excecoes:
      - Pode lancar IOError se arquivo nao pode ser escrito
      - Exception generica capturada (nao ideal, melhorar em v1.4.4)

    Nota: Usa caminho relativo (depende de onde programa e executado).
          Melhorar em v1.4.4 para usar caminho absoluto.
    """
    #try:
    with open("dados_alunos.json", "w") as dados_alunos:
        json.dump(lista_alunos, dados_alunos)
        #print("\nSalvando lista de alunos em arquivo json... ")
    #except Exception:
        # exibicao_erro(f"Erro ao salvar arquivo json {Exception}!!!")
