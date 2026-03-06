def exibir_titulo_inicial() -> None:
    """Exibição do título do projeto, para dar uma melhor experiência ao usuário, e deixar o projeto mais organizado."""
    print("\n-----  CRUD Gestão de Alunos Python  -----")
    print("--- Seja bem-vindo ao Mini-Crud em Python ---")

def exibicao_erro(erro: str) -> None:
    """Exibição de mensagens de erro, para reduzir código repetido, e exibir mensagens de erro padronizadas.

    Parâmetro: erro - mensagem de erro, para ser exibida ao usuário.

    Exibe: Mensagem de erro, que conta com um print com o erro de cada metodo que apresentar algum tipo de erro.
    """
    print(f"\nErro: {erro}")

def menu_inicial(opcao) -> None:
    """Menu executado quando se roda o projeto.
    Parâmetro: opção, que vêm -1, para início do loop, e depois passa para um input(Selecione opção), que aparece no Menu, para prosseguir.
"""

def menu_inicial_tela():
    exibir_titulo_inicial()
    print("   1 - Adicionar aluno")
    print("   2 - Atualizar aluno")
    print("   3 - Excluir aluno")
    print("   4 - Exibir aluno")
    print("   5 - Exibir todos os alunos")
    print("   6 - Salvar lista em arquivo Json")
    print("   0 - Encerrar Programa")