Projeto de Cadastro de Produtos - README
Este projeto tem como objetivo automatizar o processo de cadastro de produtos em um sistema da empresa. Utilizaremos a biblioteca pyautogui para simular ações do usuário, como clicar, escrever e pressionar teclas.

Passos do Projeto
Entrar no sistema da empresa:
Abrir o navegador (Google Chrome).
Acessar o link: https://dlp.hashtagtreinamentos.com/python/intensivao/login.
Fazer o login:
Preencher o campo de e-mail com “zetasnk@hotmail.com”.
Preencher o campo de senha com “coxinha123”.
Clicar no botão de login.
Importar a base de dados:
Utilizaremos a biblioteca Pandas para ler um arquivo CSV chamado “produtos.csv”.
A base de dados contém informações sobre os produtos a serem cadastrados.
Cadastrar um produto:
Para cada linha da tabela:
Preencher os campos de código, marca, tipo, categoria, preço unitário e custo.
Se houver observações, preencher o campo de observações.
Clicar no botão “Enviar”.
Rolar a tela para baixo para visualizar o próximo produto.
Repetir o passo 4 até cadastrar todos os produtos:
O processo será repetido para cada produto na base de dados.
Observações
O tempo de espera entre as ações (PAUSE) está configurado para 0,5 segundos.
Certifique-se de que o arquivo “produtos.csv” esteja no mesmo diretório do script.
Personalize os campos e ações conforme necessário para o sistema específico da empresa.

(Esta é a aula 1 da jornada Python do curso HASHTAG programação).
