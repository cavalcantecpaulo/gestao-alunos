def atualizar_aluno() -> None:
    """Atualização de dados de aluno."""
    rm_digitado = requisicao_aluno("atualizar")
    aluno_encontrado = busca_aluno_rm(rm_digitado)
    if aluno_encontrado is not None:
        aluno_encontrado.informacoes_aluno()
        
        nome = validacao_nome()
        curso = validacao_curso()
        mensalidade = validacao_mensalidade()

        aluno_encontrado["nome_aluno"] = nome
        aluno_encontrado["curso"] = curso
        aluno_encontrado["mensalidade"] = mensalidade

        print("\nInformações de aluno atualizada com sucesso!")
    else:
        exibicao_erro("\nRM não encontrado!!!!")

def excluir_aluno() -> None:
    """Exclusão de aluno da lista."""
    rm_digitado = requisicao_aluno("excluir")
    aluno_encontrado = busca_aluno_rm(rm_digitado)
    if aluno_encontrado is not None:
        aluno_encontrado.informacoes_aluno()
        exclusao = -1
        while exclusao !=1 and exclusao != 0:
            exclusao = int(input("\nDeseja excluir o aluno encontrado? (Digite 1 - Sim, ou 0 - Não): "))
            if exclusao == 1:
                lista_alunos.remove(aluno_encontrado)
                print("\nAluno excluído com sucesso!")
            else:
                print("\nAluno foi mantido na lista de alunos!!!")
    else:
        exibicao_erro("RM não encontrado!!!!")

def exibir_aluno() -> None:
    """Exibição de aluno específico, pelo RM."""
    rm_digitado = requisicao_aluno("exibir")
    aluno_encontrado = busca_aluno_rm(rm_digitado)
    if aluno_encontrado is not None:
        aluno_encontrado.informacoes_aluno()
    else:
        exibicao_erro("RM não encontrado!!!!")

def exibir_alunos() -> None:
    """Exibição de todos os alunos cadastrados na lista."""
    if len(lista_alunos) == 0:
        print("\nNenhum aluno encontrado!!!!")
    else:
        print("\nExibindo alunos: ")
        for aluno in lista_alunos:
            aluno.informacoes_aluno()

def requisicao_aluno(acao: str) -> int:
    """ Função padrão, usada nos inputs, que reduz código, pois é usada em diversos locais diferentes.

    Parâmetro: ação que o usuário irá realizar - (atualizar), (exibir), (excluir) - para exibir a mensagem correta ao usuário.

    Retorna: RM digitado, para ser usado na busca posteriormente. Corrigido erro que capturava string e não int
    """
    while True:
        try:
            rm = int(input(f"Digite o RM do aluno que deseja {acao}: "))
            return rm
        except ValueError:
            exibicao_erro("Digite um valor inteiro no RM!!!")

# def iniciar_lista_alunos:
#     lista_alunos = []
#     if leitura_json not null:
#       lista_alunos.append(leitura_inicial_json() not null)
#    else:
#      return None

# def leitura_inicial_json():
#     if(dados_pre_carregados !=null):
#         arquivo_json = open("../dados_alunos.json", "r")
#          dados_alunos = json.load(arquivo_json)
#          return dados_alunos
