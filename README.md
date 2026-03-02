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
    "rm": str,              # Registro de Matrícula (identificador único)
    "curso": str,           # Curso do aluno
    "mensalidade": float    # Valor da mensalidade em reais
}
```

A lista `lista_alunos\ armazena todos os dicionários de alunos cadastrados.

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

- Modularização e funções com responsabilidades claras
- Validação de RM único para integridade de dados
- Mensagens de feedback claras e consistentes
- Persistência em JSON para durabilidade dos dados
- Uso de `match/case` (Python 3.10+) para roteamento do menu
- Nomes descritivos e tratamento centralizado de erros

## 🚧 Em Desenvolvimento

Funcionalidades e melhorias continuam em desenvolvimento. Algumas melhorias recentes estão listadas abaixo.

### ✅ Implementações Recentes (v1.3.3)
- **Modularização completa das validações de entrada**
  - Separação em 4 módulos independentes: `validacao_nome()`, `validacao_rm()`, `validacao_curso()`, `validacao_mensalidade()`
  - Cada módulo encapsula a lógica de validação de um campo específico
  - Funções reutilizáveis em `adicionar_aluno()` e `atualizar_aluno()`
- Validação de RM único e evita duplicação
- Persistência em JSON com `salvando_lista_json()`
- Funções auxiliares de UI (`exibir_titulo_inicial()`)
- Tratamento centralizado de erros (`exibicao_erro()`)

## 🔮 Possíveis Próximas Adições

### Curto Prazo
- [ ] Carregamento automático de dados ao iniciar
- [ ] Validações adicionais (formatos, campos vazios)
- [ ] Busca e filtro por curso/nome/mensalidade

### Médio Prazo
- [ ] Refatoração em módulos (models, utils, views)
- [ ] Testes unitários com pytest
- [ ] Interface gráfica (tkinter/PyQt)

### Longo Prazo
- [ ] Integração com banco de dados (SQLite, PostgreSQL)
- [ ] API REST (Flask/FastAPI)
- [ ] Dashboard web

## 🎓 Conceitos e Aprendizados

Este projeto consolidou conceitos fundamentais:
- Estruturas de dados (listas e dicionários)
- Controle de fluxo e entrada interativa
- Validação e integridade de dados
- Modularização, reutilização e boas práticas de design
- Persistência com JSON e manipulação de arquivos

## 🎓 Conclusão

O projeto é uma evolução de um exercício de sala de aula que foi escalado para um pequeno sistema de Gestão de Alunos. O foco foi aplicar boas práticas de engenharia de software desde o começo, mantendo o código claro e fácil de evoluir.

---

**Status**: 🔄 Em Desenvolvimento | **Versão**: 1.3.3 | **Última atualização**: 02/03/2025
