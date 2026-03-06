

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
