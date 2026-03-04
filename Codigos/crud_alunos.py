import json
lista_alunos = []
opcao = -1

def menu_inicial(opcao):
    """Menu executado quando se roda o projeto.
    Parâmetro: opção - input (Selecione opção), que aparece no Menu.
    """

    while opcao != 0:
        exibir_titulo_inicial()
        print("   1 - Adicionar aluno")
        print("   2 - Atualizar aluno")
        print("   3 - Excluir aluno")
        print("   4 - Exibir aluno")
        print("   5 - Exibir todos os alunos")
        print("   6 - Salvar lista em arquivo Json")
        print("   0 - Encerrar Programa")
        try:
            opcao = int(input("Selecione uma opção: "))
            match opcao:
                case 1:
                    adicionar_aluno()
                case 2:
                    atualizar_aluno()
                case 3:
                    excluir_aluno()
                case 4:
                    exibir_aluno()
                case 5:
                    exibir_alunos()
                case 6:
                    salvando_lista_json()
                case 0:
                    print("\nEncerrando programa...")
                    break
                case _:
                    exibicao_erro("Opção inválida!!!")
        except ValueError:
            exibicao_erro("Valor inválido, digite um número entre as opções do menu!!!")

def informacoes_aluno(aluno):
    """Lista dados de aluno.
    Parâmetro: aluno - dicionário com os dados do aluno, para exibição organizada.
    """

    print(f"\n    Nome: {aluno["nome_aluno"]} | RM{aluno["rm"]}")
    print(f"    Curso: {aluno["curso"]} | Mensalidade: R${aluno["mensalidade"]:.2f}")

def adicionar_aluno():
    """Une todos os inputs, e cria um aluno, para depois adicionar na lista de alunos."""

    nome = validacao_nome()
    rm = validacao_rm()
    curso = validacao_curso()
    valor_mensalidade = validacao_mensalidade()

    aluno = {
        "nome_aluno": nome,
        "rm": rm,
        "curso": curso,
        "mensalidade": valor_mensalidade
    }
    lista_alunos.append(aluno)
    print("\nAluno adicionado com sucesso!")

def atualizar_aluno():
    """Atualização de dados de aluno."""

    rm_digitado = requisicao_aluno("atualizar")
    aluno_encontrado = busca_aluno_rm(rm_digitado)
    if aluno_encontrado is not None:
        print(f"\nNome: {aluno_encontrado["nome_aluno"]}")
        nome = validacao_nome()

        print(f"Curso: {aluno_encontrado["curso"]}")
        curso = validacao_curso()

        print(f"Mensalidade: R${aluno_encontrado["mensalidade"]}")
        mensalidade = validacao_mensalidade()

        aluno_encontrado["nome_aluno"] = nome
        aluno_encontrado["curso"] = curso
        aluno_encontrado["mensalidade"] = mensalidade

        print("\nInformações de aluno atualizada com sucesso!")
    else:
        exibicao_erro("\nRM não encontrado!!!!")

def excluir_aluno():
    """Exclusão de aluno da lista."""

    rm_digitado = requisicao_aluno("excluir")
    aluno_encontrado = busca_aluno_rm(rm_digitado)
    if aluno_encontrado is not None:
        print()
        lista_alunos.remove(aluno_encontrado)
        print("\nAluno excluído com sucesso!")
    else:
        exibicao_erro("\nRM não encontrado!!!!")

def exibir_aluno():
    """Exibição de aluno específico, pelo RM."""
    rm_digitado = requisicao_aluno("exibir")
    aluno_encontrado = busca_aluno_rm(rm_digitado)
    if aluno_encontrado is not None:
        informacoes_aluno(aluno_encontrado)
    else:
        exibicao_erro("\nRM não encontrado!!!!")

def exibir_alunos():
    """Exibição de todos os alunos cadastrados na lista."""
    if len(lista_alunos) == 0:
        print("\nNenhum aluno encontrado!!!!")
    else:
        print("\nExibindo alunos: ")
    for aluno in lista_alunos:
        informacoes_aluno(aluno)

def requisicao_aluno(acao):
    """ Função padrão, usada nos inputs, que reduz código, pois é usada em diversos locais diferentes.

    Parâmetro: ação que o usuário irá realizar - (atualizar), (exibir), (excluir) - para exibir a mensagem correta ao usuário.

    Retorna: RM digitado, para ser usado na busca posteriormente.
    """
    rm = input(f"Digite o RM do aluno que deseja {acao}: ")
    return rm

def salvando_lista_json():
    """Salvar lista de alunos em um arquivo Json."""
    try:
        with open("dados_alunos.json", "w") as dados_alunos:
            json.dump(lista_alunos, dados_alunos)
        print("\nSalvando lista de alunos em arquivo json... ")
    except Exception:
        exibicao_erro(f"Erro ao salvar arquivo json {Exception}!!!")

def exibir_titulo_inicial():
    """Exibição do título do projeto, para dar uma melhor experiência ao usuário, e deixar o projeto mais organizado."""
    print("\n--- CRUD Alunos Python ---")
    print("--- Seja bem-vindo ao Mini-Crud em Python ---")

def exibicao_erro(erro):
    """Exibição de mensagens de erro, para reduzir código repetido, e exibir mensagens de erro padronizadas.

    Parâmetro: erro - mensagem de erro, para ser exibida ao usuário.

    Retorna: Mensagem de erro, que conta com um print com o erro de cada método que aprersentar algum tipo de erro.
    """
    print(f"\nErro: {erro}")

def busca_aluno_rm(rm):
    """Busca aluno específico pelo RM, usado como parâmetro da função.

    Parâmetro: RM do aluno, para ser usado na busca.

    Retorna: Em caso de sucesso, o aluno com o RM utilizado.
    """
    for aluno in lista_alunos:
        if aluno["rm"] == rm:
            return aluno
    else:
        return None

def validacao_nome():
    """Validação do nome do aluno, que deve ser preenchido, e não pode conter números ou caracteres especiais.

    Retorna: Em caso de sucesso, o nome do aluno em letras maiúsculas.
    """
    nome_valido = False
    while nome_valido is False:
        nome = input("\nDigite o nome do novo aluno: ")
        condicao = ((nome == "") or (not nome.isalpha()))
        if not condicao:
            return nome.upper()
        else:
            exibicao_erro("Nome inválido!!! Digite apenas letras e não deixe o campo vazio!!!")

def validacao_rm():
    """Validação do RM do aluno, que deve ser um número inteiro,
     positivo, com no máximo 6 dígitos, e não pode ser repetido.

    Retorna: Em caso de sucesso, o RM digitado.
    """
    rm_digitado = input_rm()
    aluno_encontrado = busca_aluno_rm(rm_digitado)
    while aluno_encontrado is not None:
        exibicao_erro("RM existente!!!")
        rm_digitado = input_rm()
        aluno_encontrado = busca_aluno_rm(rm_digitado)
        if aluno_encontrado is None:
            return rm_digitado
    return rm_digitado

def validacao_curso():
    """Validação do curso que o aluno faz parte, que deve ser preenchido, e não pode ser vazio.

    Retorna: Em caso de sucesso, o nome do curso, em letras maiúsculas.
    """
    curso = input("\nDigite o novo curso do aluno: ")
    condicao = (curso == "")
    while condicao:
        curso = input("\nDigite o novo curso do aluno: ")
        if not condicao:
            return curso.upper()
    return curso.upper()

def validacao_mensalidade():
    """Validação do valor da mensalidade, que deve ser um número positivo, e não pode ser negativo.

    Retorna: Em caso de sucesso, o valor da mensalidade.
    """
    mensalidade = float(input(f"\nDigite o valor da mensalidade do aluno: "))
    condicao = mensalidade < 0
    while condicao:
            exibicao_erro("Valor de mensalidade inválido!!!")
            mensalidade = float(input(f"\nDigite o valor da mensalidade do aluno: "))
            if not condicao:
                return mensalidade
    return mensalidade

def input_rm():
    """Input específico para o RM, que reduz código repetido, e serve para validar o tipo do input,
    que deve ser inteiro, e não pode ser negativo ou ter mais de 6 dígitos.

    Retorna: Em caso de sucesso, o RM digitado.
    """
    nome_valido = False
    while nome_valido is False:
        try:
            rm = int(input(f"\nDigite o RM do aluno: "))
            if rm>0 and  len(str(rm)) < 7:
                nome_valido = True
                return rm
            else:
                exibicao_erro("RM inválido!!!")
        except ValueError:
            exibicao_erro("\nDigite um valor inteiro no RM!!!")


# def leitura_inicial_json():
#     arquivo_json = open("../dados_alunos.json", "r")
#     dados_alunos = json.load(arquivo_json)
#     return dados_alunos
#
# lista_alunos.append(leitura_inicial_json())
menu_inicial(opcao)