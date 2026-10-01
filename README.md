# Automação Python

Repositório com exemplos de automação em Python, organizados por pasta:

- **Teste1** — abre o YouTube no Microsoft Edge usando Playwright.
- **Teste2** — automatiza ações no Windows, como abrir o Bloco de Notas e o Prompt de Comando, usando PyAutoGUI.
- **Teste3** — pesquisa vídeos no YouTube e abre um resultado aleatório. A pasta `Arquivos` contém arquivos de exemplo.
- **Teste4** — organiza os arquivos da pasta `Arquivos` em subpastas conforme suas extensões.
- **Teste5** — lê dados de `clientes.xlsx` e automatiza o download de notas fiscais para uma competência informada. As dependências estão em `requirements.txt`.

## Planilha do Teste5

O arquivo `clientes.xlsx` deve ficar dentro da pasta `Teste5` e conter, na primeira planilha, estas colunas com os nomes exatamente como escritos:

- `CNPJ` — CNPJ da empresa.
- `LOGIN` — usuário de acesso ao portal.
- `SENHA` — senha de acesso ao portal.

Use uma linha para cada empresa. Preencha CNPJ, login e senha como texto, especialmente o CNPJ, para preservar zeros à esquerda. Ao iniciar o programa, informe a competência no formato `MM/AAAA`.

Arquivos `.xlsx` são ignorados pelo Git; a planilha deve ser adicionada localmente para executar o Teste5.
