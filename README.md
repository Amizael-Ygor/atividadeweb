# Projeto Flask - IFRO

Repositório da atividade acadêmica de Desenvolvimento Web III.

## Versão 1.03: Contexto Dinâmico com Jinja2

`main.py` cria a aplicação Flask `app_Amizael`. A rota `/` retorna `Olá, Turma!`, e `/saudacao/<nome>` recebe um nome pela URL. As rotas `/homepage`, `/contato` e `/index` renderizam páginas HTML. A rota `/usuario` envia `nome`, `profissao` e `disciplina` para `usuario.html`, que apresenta os valores com Jinja2.

Com a virtualenv ativada e Flask instalado, execute `python main.py` para iniciar o servidor local.

## Branch `recurso-template-base`

Neste branch, `base.html` define a estrutura compartilhada de navegação e conteúdo. `homepage.html`, `contato.html`, `index.html` e `usuario.html` estendem esse template. As rotas do `main.py` continuam usando `render_template` e não precisam de alterações para renderizar templates herdados.

## Materiais da atividade

A aplicação também usa os templates de `t_templates/` e o CSS de `static/css/estilo.css`. O logo do IFRO aparece nos templates-base, e a ilustração fornecida aparece no perfil do usuário. A homepage carrega `static/js/script2.js` para exibir data, hora e cotação; `static/js/script1.js` contém validações usadas pelos formulários de exemplo. `importando.py` demonstra a importação da função `saudacao` de `main.py`.

Os exemplos de login/API dependem de um backend externo em `127.0.0.1:8050`; eles foram extraídos, mas não são ativados pela aplicação Flask desta atividade. A chave de API que vinha no script meteorológico foi removida.