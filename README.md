# 📚 Mini CRUD de Alunos em Python

> Um projeto educacional de gerenciamento de alunos desenvolvido em Python, implementando operações CRUD (Create, Read, Update, Delete) com interface em linha de comando.

## 🎯 Sobre o Projeto

Este é um projeto criado a partir de uma **aula de Python** com o objetivo de praticar conceitos fundamentais de programação, como:
- Manipulação de estruturas de dados (listas e dicionários)
- Laços de repetição e condicionais
- Funções e modularização
- Validação de entrada do usuário
- Operações de CRUD

## ✨ Funcionalidades

O Mini CRUD oferece as seguintes operações:

### 1️⃣ **Adicionar Aluno**
- Permite registrar um novo aluno no sistema
- Solicita informações: Nome, RM (Registro de Matrícula), Curso e Mensalidade
- Armazena os dados em uma lista de dicionários

### 2️⃣ **Atualizar Aluno**
- Busca o aluno pelo RM (identificador único)
- Permite modificar: Nome, Curso e Valor da Mensalidade
- Valida se o aluno existe antes de atualizar

### 3️⃣ **Excluir Aluno**
- Remove um aluno da lista utilizando o RM
- Mensagens de confirmação quando o aluno não é encontrado

### 4️⃣ **Exibir Aluno**
- Busca e exibe os dados completos de um aluno específico
- Formatação legível com separadores visuais

### 5️⃣ **Exibir Todos os Alunos**
- Lista todos os alunos cadastrados no sistema
- Exibe mensagem quando nenhum aluno está registrado

### 6️⃣ **Salvar em JSON**
- Persiste todos os dados em arquivo `dados_alunos.json`
- Permite recuperar dados em futuras execuções do programa
- Formato de arquivo estruturado e facilmente legível

### 🚪 **Encerrar Programa**
- Fecha a aplicação de forma segura

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+** (Com a estrutura `match/case`)
- Estruturas de dados nativas (listas, dicionários)
- Interface de linha de comando (CLI)

## 📋 Pré-requisitos

- Python 3.10 ou superior instalado
- Terminal ou prompt de comando

## 🚀 Como Executar

1. Clone ou baixe o projeto:
```bash
git clone https://github.com/seu-usuario/Mini_CRUD_Python.git
cd Mini_CRUD_Python
```

2. Execute o programa:
```bash
python Codigos/crud_alunos.py
```

3. Selecione uma opção do menu e siga as instruções

## 📁 Estrutura do Projeto

```
Mini_CRUD_Python/
├── README.md
└── Codigos/
    └── crud_alunos.py
```

## 🏗️ Visão Geral da Arquitetura

O projeto é estruturado de forma modularizada com separação clara de responsabilidades. Cada função é responsável por uma operação específica do sistema.

### Estrutura de Dados Principal

```python
aluno = {
    "nome_aluno": str,      # Nome do aluno
    "rm": str,              # Registro de Matrícula (identificador único)
    "curso": str,           # Curso do aluno
    "mensalidade": float    # Valor da mensalidade em reais
}
```

A lista `lista_alunos` armazena todos os dicionários de alunos cadastrados.

### Funções Principais

#### 🎛️ **`menu_inicial(opc)`**
Função principal que controla o fluxo da aplicação. Apresenta o menu, captura a opção do usuário e chama a função correspondente usando `match/case` para roteamento de operações.

#### ➕ **`adicionar_aluno()`**
Captura as informações do aluno (nome, RM, curso e mensalidade) e adiciona à lista com feedback de sucesso.

#### ✏️ **`atualizar_aluno()`**
Busca um aluno pelo RM e permite atualizar seu nome, curso e mensalidade com valores atuais exibidos como referência.

#### ❌ **`excluir_aluno()`**
Remove um aluno específico da lista utilizando seu RM como identificador.

#### 👁️ **`exibir_aluno()`**
Exibe informações detalhadas de um aluno específico com formatação visual clara.

#### 📋 **`exibir_alunos()`**
Lista todos os alunos cadastrados no sistema ou informa quando nenhum aluno está registrado.

#### 🔍 **`requisicao_aluno(acao)`**
Função auxiliar reutilizável que solicita o RM do aluno com mensagem contextualizada sobre a ação a ser realizada. Implementa o princípio **DRY** (Don't Repeat Yourself).

#### 📊 **`informacoes_aluno(aluno)`**
Função de formatação que exibe as informações de um aluno de forma visual e padronizada com separadores.

## 🔧 Detalhes da Modularização

### Princípios Aplicados

O código segue os seguintes princípios de design:

1. **Single Responsibility Principle (SRP)**
   - Cada função tem uma responsabilidade única e bem definida
   - `adicionar_aluno()` apenas adiciona alunos
   - `atualizar_aluno()` apenas atualiza dados existentes
   - `exibir_alunos()` apenas exibe informações
   - `salvando_lista_json()` apenas persiste dados em arquivo
   - `exibir_titulo_inicial()` apenas exibe o cabeçalho
   - `exibicao_erro()` apenas formata mensagens de erro

2. **DRY (Don't Repeat Yourself)**
   - A função `requisicao_aluno(acao)` elimina a repetição de código
   - Utilizada em `atualizar_aluno()`, `excluir_aluno()` e `exibir_aluno()`
   - A função `exibicao_erro()` centraliza a exibição de mensagens de erro
   - Reduz bugs e facilita manutenção

3. **Separação de Concerns**
   - `menu_inicial()` - Controle de fluxo e roteamento de operações
   - Funções CRUD - Operações de negócio (adicionar, atualizar, excluir, exibir)
   - `informacoes_aluno()` - Apresentação/Formatação de dados
   - `requisicao_aluno()` - Utilidade de entrada/input reutilizável
   - `salvando_lista_json()` - Persistência de dados em arquivo
   - `exibicao_erro()` - Tratamento centralizado de erros
   - `exibir_titulo_inicial()` - Apresentação visual do menu

### Fluxo da Aplicação

```
┌─────────────────────────────────┐
│   menu_inicial(opc)             │
│  (Controla o fluxo principal)   │
└────────────┬────────────────────┘
             │
    ┌────────┴────────┬─────────────┬─────────────┬────────────┐
    │                 │             │             │            │
    v                 v             v             v            v
adicionar_aluno() atualizar_aluno() excluir_aluno() exibir_aluno() exibir_alunos()
    │                 │             │             │            │
    └─────────────────┴─────────────┴─────────────┴────────────┘
                      │
         ┌────────────┼────────────┐
         │            │            │
         v            v            v
   requisicao_aluno() informacoes_aluno() lista_alunos[]
   (Input auxiliar)   (Formatação)      (Dados)
```

## 💡 Boas Práticas Implementadas

✅ **Modularização do código** - Separação em funções específicas para cada operação  
✅ **Funções bem definidas** - Cada operação tem sua função responsável e reutilizável  
✅ **Menu interativo** - Interface clara e intuitiva com orientações ao usuário  
✅ **Estrutura de dados apropriada** - Uso de dicionários para armazenar informações do aluno  
✅ **Match/Case** - Alternativa moderna aos if/elif para seleção de opções (Python 3.10+)  
✅ **Mensagens de feedback otimizadas** - Feedback claro, contextualizado e informativo ao usuário  
✅ **DRY (Don't Repeat Yourself)** - Função reutilizável para requisição de RM (`requisicao_aluno`)  
✅ **Formatação visual** - Separadores e indentação para melhor legibilidade das informações  
✅ **Persistência de dados** - Salvamento de dados em arquivo JSON para recuperação posterior  
✅ **Tratamento centralizado de erros** - Função `exibicao_erro()` para mensagens padronizadas

## 🚧 Em Desenvolvimento

Este é um projeto em fase inicial de desenvolvimento com foco educacional. Funcionalidades e melhorias continuam em constante evolução, com implementações recentes focadas em modularização do código e otimização da experiência do usuário através de mensagens de feedback claras e contextualizadas.

### ✅ Implementações Recentes (v1.2.1)
- **Persistência de dados em JSON** - Função `salvando_lista_json()` para salvar dados em arquivo
- **Funções auxiliares de UI** - `exibir_titulo_inicial()` para cabeçalho padronizado
- **Tratamento centralizado de erros** - Função `exibicao_erro()` para mensagens de erro padronizadas
- **Mensagens de feedback otimizadas** - Menu intuitivo com instruções claras para melhor UX

## 🔮 Possíveis Próximas Adições

### Curto Prazo
- [ ] **Carregamento de dados ao iniciar** - Carregar alunos salvos automaticamente do arquivo JSON
- [ ] **Validação robusta** - Validar RM único, email, telefone, formato de entrada
- [ ] **Busca avançada** - Filtrar alunos por curso, nome ou intervalo de mensalidade

### Médio Prazo
- [ ] **Refatoração em módulos** - Separar em módulos (models, utils, views) para melhor organização
- [ ] **Testes unitários** - Implementar testes com pytest
- [ ] **Interface gráfica** - Migrar para tkinter ou PyQt
- [ ] **Relatórios** - Gerar relatórios em PDF com dados dos alunos
- [ ] **Autenticação** - Adicionar login de usuário

### Longo Prazo
- [ ] **Banco de dados** - Integrar SQLite, PostgreSQL ou MySQL
- [ ] **API REST** - Expor funcionalidades via API Flask/FastAPI
- [ ] **Dashboard web** - Criar interface web com Flask/Django
- [ ] **Sistema de pagamentos** - Integrar sistema de cobrança de mensalidades

## 🎓 Conceitos de Programação e Boas Práticas Aprendidas

Este projeto foi desenvolvido como exercício prático de Python, consolidando diversos conceitos fundamentais de programação e design de software:

### 📌 Conceitos Fundamentais de Programação

#### 1. **Estruturas de Dados**
- **Listas**: Armazenamento de múltiplos alunos em uma estrutura dinâmica
- **Dicionários**: Organização de dados de cada aluno com chaves nomeadas (nome, RM, curso, mensalidade)
- Compreensão de quando usar cada tipo de estrutura apropriadamente

#### 2. **Fluxo de Controle**
- **Laços de Repetição**: `while` para manter o menu ativo e `for` para iterar sobre alunos
- **Estruturas Condicionais**: `if/else` para validação e `match/case` para roteamento de opções
- Compreensão de entrada em modo interativo e saída controlada

#### 3. **Funções e Modularização**
- **Definição e chamada de funções**: Cada operação CRUD tem sua própria função
- **Funções com parâmetros**: `requisicao_aluno(acao)` mostra como parametrizar comportamento
- **Funções com retorno**: `requisicao_aluno()` retorna dados capturados
- **Escopo de variáveis**: Compreensão de variáveis locais vs globais
- **Reutilização de código**: Funções auxiliares eliminam duplicação

#### 4. **Manipulação de Dados**
- **Busca em listas**: Iterar com `for` e comparar valores com `==`
- **Modificação de dados**: Alteração de valores em dicionários dentro de listas
- **Remoção de elementos**: Uso de `remove()` para excluir alunos
- **Formatação de saída**: Concatenação de strings e `f-strings` para mensagens dinâmicas

#### 5. **Persistência de Dados**
- **Serialização JSON**: Conversão de estruturas Python para formato JSON
- **I/O de arquivos**: Abertura, escrita e fechamento de arquivos
- **Compreensão de durabilidade**: Dados salvos persistem após encerramento do programa

### 🏗️ Princípios de Design de Software

#### 1. **Single Responsibility Principle (SRP)**
Cada função tem uma única responsabilidade bem definida:
```python
adicionar_aluno()          # Apenas adiciona
atualizar_aluno()          # Apenas atualiza
excluir_aluno()            # Apenas exclui
exibir_aluno()             # Apenas exibe um
exibir_alunos()            # Apenas lista todos
salvando_lista_json()      # Apenas salva em arquivo
exibicao_erro(erro)        # Apenas formata erros
exibir_titulo_inicial()    # Apenas exibe cabeçalho
```

**Benefício**: Código mais fácil de entender, testar e modificar isoladamente.

#### 2. **DRY (Don't Repeat Yourself)**
A função `requisicao_aluno(acao)` elimina a repetição de código:
- Usada em 3 operações diferentes (atualizar, excluir, exibir)
- Uma única alteração afeta todos os lugares que a usam
- Reduz bugs e mantém o código consistente

```python
def requisicao_aluno(acao):
    rm = input(f"Digite o RM do aluno que deseja {acao}: ")
    return rm

# Reutilizada em múltiplos lugares
rmDigitado = requisicao_aluno("atualizar")
rmDigitado = requisicao_aluno("excluir")
rmDigitado = requisicao_aluno("exibir")
```

**Benefício**: Menos duplicação, mais manutenibilidade.

#### 3. **Separação de Responsabilidades (Separation of Concerns)**
O código está organizado em camadas lógicas:
- **Camada de Controle**: `menu_inicial()` - Fluxo e roteamento
- **Camada de Negócio**: Funções CRUD - Lógica de operações
- **Camada de Apresentação**: `informacoes_aluno()`, `exibicao_erro()` - Formatação
- **Camada de Utilidade**: `requisicao_aluno()` - Operações auxiliares
- **Camada de Persistência**: `salvando_lista_json()` - Armazenamento

**Benefício**: Melhor organização, facilita manutenção e futuras mudanças.

#### 4. **Coesão Alta**
Funções relacionadas fazem sentido juntas e o código é facilmente compreensível. Cada seção do código tem um propósito claro.

### 💡 Boas Práticas Técnicas

#### 1. **Estruturas de Dados Apropriadas**
- Uso de **dicionários** para dados estruturados de alunos
- Uso de **listas** para coleções dinâmicas
- Escolha consciente do tipo de dado apropriado para cada situação

#### 2. **Linguagem Moderna (Python 3.10+)**
- Uso de `match/case` em vez de `if/elif` para seleção de opções
- Mais legível e conciso que alternativas antigas
- Demonstrate compreensão de features modernas da linguagem

#### 3. **Mensagens de Feedback Claras**
- Feedback contextualizado ao usuário ("Aluno adicionado com sucesso!")
- Mensagens de erro informativas
- Menu intuitivo com orientações visuais (separadores, títulos)
- Melhora significativamente a experiência do usuário

#### 4. **Nomes Descritivos**
- Nomes de funções indicam claramente sua ação: `adicionar_aluno()`, `exibir_titulo_inicial()`, `exibicao_erro()`
- Nomes de variáveis significativos: `rmDigitado`, `lista_alunos`, `valor_mensalidade`
- Código se torna autodocumentado

#### 5. **Tratamento Centralizado de Erros**
- Função `exibicao_erro()` centraliza a formatação de mensagens de erro
- Consistência visual em todo o programa
- Fácil alterar o estilo de erro em um único lugar

#### 6. **Formatação Visual**
- Separadores visuais (linhas com hífens) melhoram legibilidade
- Indentação consistente
- Espaçamento adequado entre seções

### 🎯 Padrões de Desenvolvimento Aplicados

#### 1. **Loop de Interação (REPL-like)**
O menu em loop permite múltiplas operações sem reiniciar o programa:
```python
while opc != 0:
    # exibe menu
    # captura opção
    # executa operação
```

#### 2. **Busca Linear com Match**
Iterar sobre uma lista para encontrar elemento específico:
```python
for aluno in lista_alunos:
    if aluno["rm"] == rmDigitado:
        # fazer algo
```

#### 3. **Padrão de Validação**
Verificar condições antes de executar operações críticas

#### 4. **Roteamento Dinâmico**
`match/case` mapeia opções do usuário para funções específicas, facilitando adicionar novas operações

### 🚀 Progressão de Aprendizado

1. **Fundações**: Entender estruturas de dados e fluxo básico
2. **Funcionalidade**: Implementar operações CRUD completas
3. **Qualidade**: Refatorar para melhor código (DRY, SRP)
4. **Polimento**: Adicionar persistência e melhorar UX
5. **Profissionalismo**: Aplicar princípios de design de software

## 🎓 Conclusão

Este projeto não é apenas um exercício de programação - é uma demonstração prática de como estruturar código profissional, aplicando princípios consolidados de engenharia de software desde o início. Conceitos como modularização, separação de responsabilidades e DRY não são apenas "boas práticas teóricas", mas escolhas concretas que tornam o código mais fácil de entender, manter e evoluir.

---

**Status**: 🔄 Em Desenvolvimento | **Versão**: 1.3 | **Última atualização**: 01/03/2026

