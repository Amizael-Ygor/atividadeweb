# Projeto Flask - IFRO

Repositório da atividade acadêmica de Desenvolvimento Web III.

## Versão 1.03: Contexto Dinâmico com Jinja2

`main.py` cria a aplicação Flask `app_Amizael`. A rota `/` retorna `Olá, Turma!`, e `/saudacao/<nome>` recebe um nome pela URL. As rotas `/homepage`, `/contato` e `/index` renderizam páginas HTML. A rota `/usuario` envia `nome`, `profissao` e `disciplina` para `usuario.html`, que apresenta os valores com Jinja2.

Com a virtualenv ativada e Flask instalado, execute `python main.py` para iniciar o servidor local.