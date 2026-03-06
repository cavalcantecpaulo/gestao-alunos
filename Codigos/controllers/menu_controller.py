"""
Controller de Menu: Orquestra o fluxo da aplicacao.

Responsabilidades:
  - Conectar View (coleta dados) com Service (valida) com Repository (persiste)
  - Processar opcoes do menu e chamar handlers apropriados
  - Gerenciar fluxo de erros e feedback ao usuario

Fluxo tipico:
  1. View coleta dados do usuario (input_aluno)
  2. Controller envia para Service validar cada campo
  3. Se valido, Controller chama Repository para persistir
  4. Controller exibe resultado (sucesso ou erro)

Regras de imports:
  - Importa View (para coletar dados)
  - Importa Service (para validar)
  - Importa Repository (para persistir)
  - NAO importa Model diretamente (Service faz isso)
"""
from Codigos.repositories.aluno_repository import lista_alunos
from Codigos.services.aluno_service import validar_nome, validar_mensalidade, validar_curso, validar_rm, \
    criar_objeto_aluno
from Codigos.views.aluno_view import input_aluno


def escolha_usuario():
    """
    Captura opcao do usuario no menu principal.

    Retorna: Numero inteiro da opcao escolhida.

    Nota: Ainda nao trata ValueError (usuario digita texto em vez de numero).
          Corrigir em v1.4.4 para envolver em try/except.
    """
    opcao = int(input("Selecione uma opção: "))
    match opcao:
        case 1: adicionar_aluno()
        case 2: atualizar_aluno()
        case 3: excluir_aluno()
        case 4: exibir_aluno()
        case 5: exibir_alunos()
        case 6: salvando_lista_json()
        case 0: print("\nEncerrando programa...")
        case _: exibicao_erro("Opção inválida!!!")
    return opcao
        #except ValueError:
            #exibicao_erro("Valor inválido, digite um número entre as opções do menu!!!")

def adicionar_aluno():
    """
    Handler para opcao 1: Adicionar Aluno.

    Fluxo:
      1. View coleta dados (nome, rm, curso, mensalidade)
      2. Service valida cada campo individualmente
      3. Se algum invalido, exibe erro e retorna (nao persiste)
      4. Se todos validos, Repository adiciona na lista
      5. Exibe mensagem de sucesso
    """
    try:
        dados_aluno = input_aluno()
        if not validar_nome(dados_aluno["nome_aluno"]):
            print("Nome inválido!!!")
            return

        if not validar_rm(dados_aluno["rm"]):
            print("RM Inválido!!!")
            return

        if not validar_curso(dados_aluno["curso"]):
            print("Curso inválido!!!")
            return

        if not validar_mensalidade(dados_aluno["mensalidade"]):
            print("Valor de mensalidade inválida!!!")
            return

        aluno = criar_objeto_aluno(dados_aluno["nome_aluno"], dados_aluno["rm"], dados_aluno["curso"], dados_aluno["mensalidade"])
        lista_alunos.append(aluno)
    except ValueError:
        print("Valor inválido, digite corretamente!!!")
