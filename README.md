# 📚 Gestão de Alunos — Projeto em Python

> Projeto educacional para gerenciamento de alunos em Python (operações CRUD) com interface em linha de comando.

## 🎯 Sobre o Projeto

Este projeto nasceu a partir de uma atividade em aula na disciplina "Computational Thinking Using Python" e foi escalado pessoalmente para um sistema de Gestão de Alunos. A ideia inicial — um mini-CRUD estudado em sala — serviu para praticar listas e dicionários após conceitos apresentados em aulas anteriores. Desenvolvi melhorias e refinamentos no código durante o início do meu segundo semestre na FIAP.

O objetivo é consolidar conceitos fundamentais de programação, como:
- Manipulação de estruturas de dados (listas e dicionários)
- Laços de repetição e condicionais
- Funções e modularização
- Validação de entrada do usuário
- Operações de CRUD (Create, Read, Update, Delete)

## ✨ Funcionalidades

O sistema de Gestão de Alunos oferece as seguintes operações:

### 1️⃣ **Adicionar Aluno**
- Registrar um novo aluno no sistema
- Informações solicitadas: Nome, RM (Registro de Matrícula), Curso e Mensalidade
- Validação de RM único — impede duplicação de registros de matrícula
- Armazenamento em uma lista de dicionários

### 2️⃣ **Atualizar Aluno**
- Busca por RM (identificador único)
- Permite alterar Nome, Curso e Mensalidade
- Valida existência do aluno antes de atualizar

### 3️⃣ **Excluir Aluno**
- Remove um aluno a partir do RM
- **Confirmação de exclusão**: solicita confirmação do usuário antes de remover (1 - Sim, 0 - Não)
- Mensagens claras quando o aluno não é encontrado

### 4️⃣ **Exibir Aluno**
- Exibe dados completos de um aluno específico com formatação legível

### 5️⃣ **Exibir Todos os Alunos**
- Lista todos os alunos cadastrados
- Mensagem informativa quando não houver registros

### 6️⃣ **Salvar em JSON**
- Persiste os dados no arquivo `dados_alunos.json`
- Permite recuperar o estado em execuções futuras

### 🚪 **Encerrar Programa**
- Encerra a aplicação com segurança

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+** (uso de `match/case` no menu)
- Estruturas de dados nativas (listas, dicionários)
- Interface de linha de comando (CLI)

## 📋 Pré-requisitos

- Python 3.10 ou superior instalado
- Terminal ou prompt de comando

## 🚀 Como Executar

1. Clone ou baixe o projeto (exemplo):

```powershell
git clone https://github.com/cavalcantecpaulo/gestao_alunos.git; cd gestao_alunos
```

2. Execute o programa a partir da pasta do repositório:

```powershell
python Codigos/crud_alunos.py
```

3. Selecione uma opção do menu e siga as instruções.

> Observação: o arquivo principal do código está localizado em `Codigos/crud_alunos.py` — o caminho acima corresponde à estrutura do repositório.

## 📁 Estrutura do Projeto

```
gestao_alunos/
├── README.md
└── Codigos/
    └── crud_alunos.py
```

## 🏗️ Visão Geral da Arquitetura

O código foi organizado com separação clara de responsabilidades. Cada função tem uma responsabilidade definida, seguindo princípios de design como SRP e DRY.

### Estrutura de Dados Principal

```python
aluno = {
    "nome_aluno": str,      # Nome do aluno
    "rm": int,              # Registro de Matrícula (identificador único)
    "curso": str,           # Curso do aluno
    "mensalidade": float    # Valor da mensalidade em reais
}
```

A lista `lista_alunos` armazena todos os dicionários de alunos cadastrados.

### Funções Principais (resumo)

#### Controle e Roteamento
- `menu_inicial(opc)` — controle de fluxo principal com roteamento via `match/case`

#### Operações CRUD
- `adicionar_aluno()` — captura e adiciona um novo aluno com validação
- `atualizar_aluno()` — atualiza dados de um aluno existente por RM
- `excluir_aluno()` — remove aluno da lista por RM
- `exibir_aluno()` — exibe informações detalhadas de um aluno por RM
- `exibir_alunos()` — lista todos os alunos cadastrados

#### Validação de Entrada (Módulos Separados — v1.3.3)
- `validacao_nome()` — valida e captura o nome do aluno (evita vazios)
- `validacao_rm()` — valida RM único, evita duplicação
- `input_rm()` — função auxiliar para captura de RM (suporta reutilização)
- `validacao_curso()` — valida e captura o curso (evita vazios, retorna em maiúsculas)
- `validacao_mensalidade()` — valida valor numérico positivo para mensalidade

#### Funções Auxiliares
- `requisicao_aluno(acao)` — solicita RM de forma contextualizada (DRY)
- `informacoes_aluno(aluno)` — formata a exibição de dados com separadores
- `exibir_titulo_inicial()` — exibe cabeçalho da aplicação
- `exibicao_erro(erro)` — trata exibição centralizada de erros
- `salvando_lista_json()` — persiste dados em `dados_alunos.json`

## 🔧 Detalhes da Modularização

### Princípios Aplicados

1. **Single Responsibility Principle (SRP)** — cada função cumpre uma única responsabilidade clara.
   - Validação de nome, RM, curso e mensalidade estão em módulos separados
   - Operações CRUD são independentes e reutilizam os módulos de validação
   - Funções auxiliares (erro, exibição, persistência) com responsabilidades bem definidas

2. **DRY (Don't Repeat Yourself)** — funções auxiliares eliminam duplicação.
   - `validacao_nome()`, `validacao_rm()`, `validacao_curso()`, `validacao_mensalidade()` são reutilizadas em `adicionar_aluno()` e `atualizar_aluno()`
   - `requisicao_aluno(acao)` centraliza a captura de RM com contexto dinâmico
   - `informacoes_aluno(aluno)` formata exibição consistente

3. **Separação de Concerns** — controle, negócio, apresentação e persistência bem definidos.
   - **Controle**: `menu_inicial()` roteia operações
   - **Validação**: Módulos separados para cada campo
   - **Negócio**: CRUD (adicionar, atualizar, excluir, exibir)
   - **Apresentação**: `informacoes_aluno()`, `exibir_titulo_inicial()`, `exibicao_erro()`
   - **Persistência**: `salvando_lista_json()`

### Modularização de Validação de Entrada (v1.3.3)

A partir da v1.3.3, as **4 validações principais** foram separadas em funções dedicadas:

```
Adicionar/Atualizar Aluno
    ├── validacao_nome()           → Valida nome (evita vazio)
    ├── validacao_rm()             → Valida RM único (chama input_rm())
    ├── validacao_curso()          → Valida curso (evita vazio, maiúsculas)
    └── validacao_mensalidade()    → Valida valor positivo
```

Benefícios:
- ✅ Facilita testes isolados de cada validação
- ✅ Reutilização em múltiplas operações (adicionar e atualizar)
- ✅ Manutenção centralizada de regras de validação
- ✅ Código mais legível e organizado

### Fluxo da Aplicação (visão simplificada)

Resumo do fluxo (apenas texto, versão limpa e legível):

1. `menu_inicial(opc)` — apresenta o menu CLI e roteia para a operação escolhida.

2. Operações principais:
   - `adicionar_aluno()`
     - Captura dados (nome, RM, curso, mensalidade)
     - Adiciona dicionário à `lista_alunos`
     - (Opcional) chama `salvando_lista_json()` para persistir alterações

   - `atualizar_aluno()`
     - Usa `requisicao_aluno("atualizar")` para obter o RM
     - Localiza aluno na `lista_alunos` e atualiza campos
     - Chama `salvando_lista_json()` para persistir alterações

   - `excluir_aluno()`
     - Usa `requisicao_aluno("excluir")` para obter o RM
     - Remove aluno da `lista_alunos` se existir
     - Chama `salvando_lista_json()` para persistir alterações

   - `exibir_aluno()`
     - Usa `requisicao_aluno("exibir")` para obter o RM
     - Exibe os dados formatados via `informacoes_aluno(aluno)`

   - `exibir_alunos()`
     - Itera por `lista_alunos` e exibe cada registro

3. Funções auxiliares chave:
   - `requisicao_aluno(acao)` — entrada centralizada para solicitar RM
   - `informacoes_aluno(aluno)` — formata saída para leitura amigável
   - `salvando_lista_json()` — persistência em `dados_alunos.json` (opcional)

4. Observações:
   - O fluxo do menu é independente da existência do arquivo `dados_alunos.json` — se o arquivo não existir, o programa pode iniciar com `lista_alunos` vazia.

## 💡 Boas Práticas Implementadas

### Para o Código
- **Modularização robusta**: cada função tem responsabilidade clara e bem definida
- **Validação de integridade**: RM único impede registros de matrícula duplicados
- **Feedback consistente**: mensagens claras em operações e erros
- **Persistência de dados**: arquivos JSON para durabilidade entre execuções
- **Estruturas Python modernas**: uso de `match/case` (Python 3.10+) para roteamento elegante
- **Nomes descritivos**: variáveis e funções com nomes semanticamente significativos
- **Tratamento centralizado de erros**: função `exibicao_erro()` padroniza mensagens
- **Tipos consistentes**: dicionários bem estruturados para representar dados

### Para a Codificação
- **Validação em camadas**: cada campo de entrada tem sua própria função de validação independente
- **Reutilização de código**: funções auxiliares como `requisicao_aluno()` e `busca_aluno_rm()` reduzem duplicação
- **Separação de responsabilidades**: entrada, processamento e exibição bem segregados
- **Legibilidade**: estruturas simples e fáceis de acompanhar, sem complexidade desnecessária
- **Escalabilidade**: organização permite crescimento sem refatorações maiores
- **Validação preventiva**: erros capturados na entrada, antes de afetar estado (v1.3.7+)
- **Loop iterativo com flags**: padrão consistente em validações para melhor controle (v1.3.6-v1.3.7)

### Padrões de Implementação Consolidados (v1.3.7+)

#### Padrão de Validação com Loop e Flag
```python
# Exemplo: validacao_nome()
nome_valido = False
while nome_valido is False:
    nome = input("\nDigite o nome do aluno: ")
    condicao = ((nome == "") or (not nome.isalpha()))
    if not condicao:
        nome_valido = True
        return nome.upper()
    else:
        exibicao_erro("Nome inválido!!! Digite apenas letras...")
```

#### Padrão de Try/Except em Conversão de Tipo
```python
# Exemplo: input_rm()
nome_valido = False
while nome_valido is False:
    try:
        rm = int(input(f"\nDigite o RM do aluno: "))
        if rm > 0 and len(str(rm)) < 7:
            return rm
        else:
            exibicao_erro("RM inválido!!!")
    except ValueError:
        exibicao_erro("\nDigite um valor inteiro no RM!!!")
```

#### Padrão de Validação de Mensalidade (v1.3.7)
```python
# Tratamento robusto com try/except + validação de valor
try:
    mensalidade = float(input(f"\nDigite o valor da mensalidade: "))
    condicao = mensalidade < 0
    while condicao:
        exibicao_erro("Valor de mensalidade inválido!!!")
        mensalidade = float(input(f"\nDigite novamente: "))
        if not condicao:
            return mensalidade
    return mensalidade
except ValueError:
    exibicao_erro("Digite um valor numérico válido!!!")
```

#### Padrão de Persistência com Tratamento de Erro
```python
# Exemplo: salvando_lista_json()
def salvando_lista_json():
    try:
        with open("dados_alunos.json", "w") as dados_alunos:
            json.dump(lista_alunos, dados_alunos)
        print("\nSalvando lista de alunos em arquivo json...")
    except Exception:
        exibicao_erro(f"Erro ao salvar arquivo json!!!")
```

#### Padrão de Busca com None Check
```python
# Exemplo: busca_aluno_rm()
def busca_aluno_rm(rm):
    for aluno in lista_alunos:
        if aluno["rm"] == rm:
            return aluno
    return None

# Uso padrão em operações CRUD
aluno_encontrado = busca_aluno_rm(rm_digitado)
if aluno_encontrado is not None:
    # processar aluno
else:
    exibicao_erro("\nRM não encontrado!!!!")
```

### Convenções de Nomenclatura Consolidadas (v1.3.7+)
- **Funções de validação**: prefixo `validacao_` (ex: `validacao_nome()`, `validacao_rm()`)
- **Funções auxiliares de input**: prefixo `input_` (ex: `input_rm()` — input específico para RM)
- **Funções de busca**: prefixo `busca_` (ex: `busca_aluno_rm()`)
- **Funções de exibição**: prefixo `exibir_` ou `exibicao_` (ex: `exibir_aluno()`, `exibicao_erro()`)
- **Funções de persistência**: prefixo `salvando_` ou `carregando_` (ex: `salvando_lista_json()`)
- **Variáveis de controle**: sufixo `_valido` ou `_encontrado` (ex: `nome_valido`, `aluno_encontrado`)
- **Dicionários de dados**: nomes no singular (ex: `aluno`) para representar estrutura individual
- **Listas de dados**: nomes no plural (ex: `lista_alunos`) para representar coleção



### Limitações Conhecidas

1. **Ausência de carregamento automático**: dados em JSON não são carregados ao iniciar
   - A função `leitura_inicial_json()` está comentada no final do código
   - Usuário começa com lista vazia a cada execução
   - **Solução futura**: Descomente e adicione try/except com fallback para lista vazia

2. **Sem backup de dados**: `salvando_lista_json()` sobrescreve sem cópia de segurança
   - Risco de perda de dados se processo for interrompido
   - **Solução futura**: Criar backup com timestamp antes de sobrescrever

3. **Busca linear**: `busca_aluno_rm()` usa O(n) complexity
   - Aceitável para <1000 alunos
   - Inadequado em produção com muitos registros
   - **Solução futura**: Usar banco de dados com índices

4. **Sem type hints**: Assinaturas de função sem anotações de tipo
   - Dificulta compreensão de tipos esperados
   - **Solução futura**: Adicionar type hints em v1.5.0

### Tratamento de Exceções Atual (v1.4.1)

| Função | ValueError | FileError | Status |
|--------|-----------|-----------|--------|
| `menu_inicial()` | ✅ Capturado (v1.4.1) | ❌ Não | ✅ Robusto |
| `input_rm()` | ✅ Capturado | ❌ Não | Bom |
| `validacao_mensalidade()` | ✅ Capturado | ❌ Não | ✅ Robusto (v1.3.7) |
| `salvando_lista_json()` | ✅ Capturado | ✅ Capturado | ✅ Robusto |

### Regras e Convenções de Implementação (v1.3.7+)
- **RM único**: `validacao_rm()` impede duplicação; `busca_aluno_rm()` opera de forma rápida e segura
- **Campos obrigatórios**: `nome_aluno`, `rm`, `curso`, `mensalidade` — validação evita vazios e tipos inválidos
- **Normalização de dados**:
  - Campo `nome_aluno` armazenado em MAIÚSCULAS (padronização visual)
  - Campo `curso` em MAIÚSCULAS (facilita buscas e comparações futuras)
  - RM mantém tipo numérico internamente para validações de intervalo
  - Mensalidade sempre como `float` para operações monetárias precisas
- **Tratamento robusto de exceções**: 
  - `ValueError` capturado em `input_rm()`, `validacao_mensalidade()` evita crashes (v1.3.6-v1.3.7)
  - Try/except em `salvando_lista_json()` para erros de I/O (v1.3.6+)
  - Exceções genéricas com mensagem clara ao usuário
- **Persistência JSON**: 
  - `salvando_lista_json()` serializa `lista_alunos` com tratamento de erro
  - Arquivo `dados_alunos.json` criado automaticamente ou sobrescrito (sem backup em v1.3.7)
  - Ponto de melhoria: adicionar backup com timestamp em v1.4.0
- **UX/UI consistente**: 
  - Prefixos de erro padronizados via `exibicao_erro()`
  - Confirmações claras em operações bem-sucedidas
  - Mensagens descritivas orientam usuário em caso de erro
- **Docstrings em todas as funções** (v1.3.6+):
  - Padrão consolidado com descrição, parâmetros e retorno
  - Facilita manutenção e compreensão do código

## 📌 Exemplo de Uso Completo

### Cenário: Adicionar e Exibir um Aluno

```bash
$ python Codigos/crud_alunos.py

--- CRUD Alunos Python ---
--- Seja bem-vindo ao Mini-Crud em Python ---

   1 - Adicionar aluno
   2 - Atualizar aluno
   3 - Excluir aluno
   4 - Exibir aluno
   5 - Exibir todos os alunos
   6 - Salvar lista em arquivo Json
   0 - Encerrar Programa

Selecione uma opção: 1

Digite o nome do novo aluno: João Silva
Digite o RM do aluno: 123456
Digite o novo curso do aluno: Engenharia de Software  
Digite o valor da mensalidade do aluno: 1250.50

Aluno adicionado com sucesso!

--- CRUD Alunos Python ---
--- Seja bem-vindo ao Mini-Crud em Python ---

   1 - Adicionar aluno
   2 - Atualizar aluno
   [...]

Selecione uma opção: 4

Digite o RM do aluno que deseja exibir: 123456

    Nome: JOÃO SILVA | RM123456
    Curso: ENGENHARIA DE SOFTWARE | Mensalidade: R$1250.50

[...]

Selecione uma opção: 6

Salvando lista de alunos em arquivo json... 

Selecione uma opção: 0

Encerrando programa...
```

### Resultado em `dados_alunos.json`:

```json
[
  {
    "nome_aluno": "JOÃO SILVA",
    "rm": 123456,
    "curso": "ENGENHARIA DE SOFTWARE",
    "mensalidade": 1250.5
  }
]
```


## 🚧 Em Desenvolvimento

Funcionalidades e melhorias continuam em desenvolvimento. Algumas melhorias recentes estão listadas abaixo.

### ✅ Implementações Mais Recentes (v1.4.1)

- **Confirmação antes de excluir aluno** ✅ Implementado
  - Nova camada de segurança na função `excluir_aluno()`
  - Solicita confirmação do usuário (1 - Sim, 0 - Não)
  - Evita exclusões acidentais de registros
  - Implementa o padrão de loop com validação para input de confirmação
  - Mensagem clara de exclusão bem-sucedida ou cancelada

- **Tratamento de ValueError no Menu Inicial** ✅ Implementado
  - `menu_inicial()` agora captura `ValueError` para entrada inválida
  - Evita crash quando usuário digita texto em vez de números
  - Mensagem de erro descritiva: "Valor inválido, digite um número entre as opções do menu!!!"
  - Melhora robustez geral da aplicação

- **Refatoração de `validacao_nome()`** ✅ Implementado
  - Validação simplificada: agora verifica apenas se o campo não está vazio
  - Remove restrição de `isalpha()` que impedia nomes com espaços (ex: "Maria Silva")
  - Mantém conversão para MAIÚSCULAS
  - Melhora usabilidade permitindo nomes completos

### ✅ Implementações Recentes (v1.3.7)

- **Tratamento de ValueError em `validacao_mensalidade()`** ✅ Implementado
  - Conversão `float()` agora envolvida em try/except
  - Loop iterativo com mensagem de erro descritiva
  - Validação de valor negativo como fallback secundário
  - Evita crash completo ao digitar letras ou símbolos
  - Padrão consolidado para futuras validações numéricas

### ✅ Implementações Recentes (v1.3.6)
- **Docstrings completas em todas as funções**
  - Padrão de documentação consolidado e consistente
  - Documentação de parâmetros e retorno bem definida
  - Facilita manutenção futura e entendimento do código

- **Try/except robusto em persistência JSON**
  - `salvando_lista_json()` agora trata exceções de arquivo e I/O
  - Captura erros de escrita em disco e exibe mensagem amigável ao usuário
  - Evita crashes e perda de dados em caso de problemas de sistema de arquivos

- **Correção de fluxo em validação de mensalidade**
  - Lógica refatorada para capturar valor **antes** da verificação de condição
  - Tratamento robusto de `ValueError` para entradas não numéricas
  - Loop iterativo com flag booleano para melhor controle
  - Evita crash ao usuário digitar valores inválidos (ex: letras, símbolos)

- **Melhoria de input e validação de RM**
  - RM agora retorna `str` (não `int`) para consistência com código
  - Validação aprimorada: `isdigit()` + range (1 a 999999) + máximo 6 dígitos
  - Tratamento de `ValueError` abrangente em `input_rm()`
  - Variável de controle renomeada para clareza semântica

### ✅ Implementações Anteriores (v1.3.5)
- **Modularização completa das validações de entrada**
  - Manutenção das 4 validações independentes: `validacao_nome()`, `validacao_rm()`, `validacao_curso()`, `validacao_mensalidade()` (reutilizáveis).
- **Inclusão da função interna `busca_aluno_rm(rm)`**
  - Finalidade: localizar e retornar o dicionário do aluno a partir do RM informado; usada por `atualizar_aluno()`, `excluir_aluno()` e `exibir_aluno()`.
- **Melhorias de robustez e UX**
  - Mensagens de erro mais claras, confirmação de ações e validação preventiva no input.
- **Persistência/Arquivos**
  - `salvando_lista_json()` para exportar os dados; sugestão de carregamento inicial automático (próxima melhoria).

## 🚧 Histórico de Versões & Roadmap

### ✅ Versão Atual (v1.4.1)
**Status**: 🟢 Funcional e estável

**Funcionalidades implementadas**:
- ✅ CRUD completo (Create, Read, Update, Delete)
- ✅ Menu interativo com `match/case`
- ✅ Validação modularizada em 4 funções dedicadas
- ✅ Persistência robusta em JSON com try/except
- ✅ Busca por RM único
- ✅ Tratamento centralizado de erros
- ✅ Docstrings completas em todas as funções
- ✅ Validação de mensalidade corrigida e melhorada
- ✅ Tratamento de ValueError em `validacao_mensalidade()`
- ✅ **Confirmação antes de excluir aluno** (v1.4.1)
- ✅ **Tratamento de ValueError no Menu Inicial** (v1.4.1)
- ✅ **Refatoração de validacao_nome() para permitir nomes completos** (v1.4.1)

### 🔄 Roadmap de Melhorias

#### ✅ Última Release (v1.4.1) — Segurança e Robustez
**Status**: 🟢 Concluída

- [x] Confirmação antes de excluir aluno — ✅ Implementado em v1.4.1
  - ✅ Loop de validação com input 1/0
  - ✅ Evita exclusões acidentais
  - ✅ Feedback claro ao usuário
- [x] Tratamento de ValueError no menu — ✅ Implementado em v1.4.1
  - ✅ Try/except no menu_inicial()
  - ✅ Mensagem de erro descritiva
- [x] Refatoração de validacao_nome() — ✅ Implementado em v1.4.1
  - ✅ Permite nomes com espaços
  - ✅ Mantém conversão para MAIÚSCULAS

#### 🎯 Próximo Release (v1.4.2) — Melhorias de UX
**Foco**: Aprimorar experiência do usuário

- [ ] Melhorar formatação de saída (tabelas ASCII, índices visuais)
- [ ] Adicionar mais validações (ex: CPF, formato de e-mail)
- [ ] Sistema de logs de operações

#### 🎯 Curto Prazo (v1.5.0) — Consolidação
**Foco**: Estabilidade, funcionalidade 100%, melhorias QoL

- [ ] Implementar `leitura_inicial_json()` com fallback automático
  - Carregamento de dados ao inicializar aplicação
  - Try/except com graceful fallback para lista vazia
- [ ] Sistema de backup automático antes de sobrescrever JSON
- [ ] Type hints em assinaturas de funções
- [ ] Linting com flake8 — verificação de style
- [ ] Testes unitários iniciais com pytest (cobertura mínima 60%)

#### 📋 Médio Prazo (v1.5.0 - v2.0.0) — Modularização

**Arquitetura**:
- [ ] Refatorar em submódulos: `models/`, `validators.py`, `crud_operations.py`, `persistence.py`
- [ ] Criar classe `Aluno` com validação integrada
- [ ] Padrão Repository para persistência
- [ ] Separar UI da lógica de negócio

**Qualidade**:
- [ ] Testes unitários com pytest
- [ ] Cobertura mínima 80%
- [ ] Type hints e linting (flake8)
- [ ] Testes de integração CRUD

**Dados**:
- [ ] Suporte a múltiplos formatos (CSV, XML)
- [ ] Sistema de backup automático
- [ ] Validação ao carregar JSON

#### 🚀 Longo Prazo (v2.5.0+) — Escalabilidade

**Banco de Dados**:
- [ ] SQLite com índices de busca
- [ ] Migrações com Alembic
- [ ] PostgreSQL para produção

**Interface**:
- [ ] GUI com Tkinter/PySimpleGUI
- [ ] Dashboard web com Flask
- [ ] Relatórios em PDF

**API e Deploy**:
- [ ] REST API com FastAPI
- [ ] Autenticação JWT
- [ ] Docker e CI/CD

**Advanced**:
- [ ] Busca avançada com filtros
- [ ] Paginação para grandes datasets
- [ ] Histórico de alterações
- [ ] Exportação para Excel

## 🎓 Conceitos e Aprendizados

Este projeto consolidou conceitos fundamentais de programação e engenharia de software:

### Programação Python
- **Estruturas de dados nativas**: listas para coleções, dicionários para estruturação de dados
- **Controle de fluxo**: loops `while`, condicionais `if/else`, `match/case` para roteamento robusto
- **Funções**: definição, parâmetros, return values, escopo local e global
- **Entrada/Saída**: `input()` para CLI, `print()` formatado com f-strings
- **Tratamento de exceções**: try/except para `ValueError` e possíveis crashes
- **Manipulação de arquivos**: leitura e escrita com `open()`, serialização JSON com `json` module

### Engenharia de Software
- **Modularização**: divisão de responsabilidades em funções pequenas e testáveis
- **Single Responsibility Principle (SRP)**: cada função faz uma coisa bem
- **DRY (Don't Repeat Yourself)**: reutilização de código via funções auxiliares
- **Separação de Concerns**: lógica de validação, CRUD, persistência isoladas
- **Integridade de dados**: RM único, validação em múltiplas camadas, estruturação com dicionários
- **Nomeação significativa**: identificadores claros facilitam compreensão e manutenção

### Boas Práticas Aplicadas
- **Validação entrada do usuário**: não confiar em entrada externa, validar tipos e valores
- **Mensagens de erro descritivas**: feedback claro ajuda diagnóstico e UX
- **Persistência de dados**: JSON para durabilidade entre execuções
- **Organização de código**: estrutura hierárquica, lógica linear fácil de acompanhar
- **Testabilidade**: funções independentes facilitam testes isolados futuros
- **Escalabilidade**: arquitetura permite expansão com pouca refatoração

### Lições Aprendidas
1. **Começar pequeno**: Exercício em aula → MVP funcional → Sistema robusto
2. **Princípios importam**: SRP e DRY fazem código mais legível e manutenível
3. **Validação cedo**: Capturar erros na entrada é mais fácil que recuperar depois
4. **Estrutura de dados apropriada**: Dicionário é perfeito para representar aluno (chaves significativas)
5. **Persistência é essencial**: JSON permite continuidade entre execuções
6. **Feedback ao usuário**: Mensagens claras melhoram experiência e confiança
7. **Modularização antes de crescimento**: Funções modulares facilitam testes e futuras integrações

## 🤝 Como Contribuir / Estender o Projeto

Se quiser expandir ou melhorar este projeto:

1. **Para adicionar funcionalidades**:
   - Crie funções seguindo padrão SRP (uma responsabilidade por função)
   - Adicione novo `case` em `menu_inicial()` se for operação CRUD
   - Reutilize validações existentes quando possível
   - Teste manualmente antes de commitar

2. **Para melhorar validações**:
   - Modifique a função de validação correspondente
   - Mantenha mensagens de erro descritivas
   - Documente mudanças significativas no README

3. **Para iterar sobre limitações**:
   - Consulte a seção "Limitações e Pontos de Atenção"
   - Consulte o "Roadmap" para priorização
   - Siga o plano de versões sugerido

4. **Para refatorar**:
   - Mantenha testes do CRUD funcionais após mudanças
   - Preserve nomes de funções públicas
   - Adicione docstrings quando refatorar

## 📚 Referências e Recursos

### Python Docs
- [Data Structures (Lists, Dicts)](https://docs.python.org/3/tutorial/datastructures.html)
- [Control Flow (`match/case`)](https://docs.python.org/3/tutorial/controlflow.html#match-statements)
- [Built-in `json` module](https://docs.python.org/3/library/json.html)
- [Exception Handling](https://docs.python.org/3/tutorial/errors.html)

### Princípios de Engenharia
- SOLID Principles (SRP, OCP, LSP, ISP, DIP)
- DRY (Don't Repeat Yourself)
- KISS (Keep It Simple, Stupid)
- Clean Code by Robert C. Martin

## 🎓 Conclusão

O projeto é uma evolução de um exercício de sala de aula que foi escalado para um pequeno sistema de Gestão de Alunos. O foco foi aplicar **boas práticas de engenharia de software desde o começo**, mantendo o código:

- ✅ **Claro**: fácil de ler e entender
- ✅ **Fácil de evoluir**: modularizado, sem grandes dependências
- ✅ **Testável**: funções isoladas e responsabilidades bem definidas
- ✅ **Escalável**: estrutura permite crescimento sem refatorações maiores

O sistema atual é funcional e atende aos objetivos educacionais, servindo como base sólida para futuras expansões e aprendizados mais avançados em programação.

---

**Status**: 🟢 Funcional e Estável/Em Desenvolvimento | **Versão**: 1.4.2 | **Última atualização**: 05/03/2026
