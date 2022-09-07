# Introdução
Essa aplicação tem como intuito gerenciar as vulnerabilidades do top 10 OWASP, permitindo que o usuario realize as funções de um CRUD (criar, ler, editar e deletar). Para adicionar ao banco de dados basta enviar um formulário na página de registro, que caso passe por todas validações é adicionado um novo item no nosso banco de dados, para lear os items do banco de dados devemos ir para página de visualização, na qual é exibida uma tabela com todos os items do nosso banco de dados, dentro dessa tabela já temos um link para as outras duas opções do CRUD, editar e deletar. Clicando no icone de lápis vamos ser redirecionado para um formulário de edição do item clicado, já clicando no icone de "X", vamos ser redirecionados para uma página para confirmação do usuario se ele realmente quer deletar aquele item que ele selecionou.

# Ferramentas utilizadas
Web aplication desenvolvida com Python utilizando Django como back-end, Bootstrap utilizado no front-end da aplicação, banco de dados utilizado é em sqlite3 e a SGDB escolhida foi o Django Administration.

# Let's Start
## Criação do projeto
Primeiro vamos precisar instalar as ferramentas utilizadas no projetos, através do comando "pip" do Python vamos instalar o Django e baixar a pasta static que contem o nosso Bootstrap para ser utilizado no estilo da nossa página.

Após instalar essas ferramentas será necessário criar um projeto para nossa web aplication, crie uma pasta para armazenar seu projeto e rode o comando: 

    "django-admin.py startproject *NOME_DO_PROJETO*"
    
Em seguida vamos criar o nosso aplicativo, que é o responsavel pelas configurações do back-end e banco de dados, basta entrar na pasta do projeto que foi criada com o primeiro comando e rodar o seguinte comando, "python manage.py startapp *NOME_DO_APP*"
    
## Configuração do projeto
Seguindo para a configuração do nosso projeto, devemos ir dentro da pasta do projeto (a que criamos com o primeiro comando) e abrir o arquivo "urls.py", com esse arquivo podemos manipular as URLs que estaram no nosso site. Dentro do array urlpatterns adicione outro path da nossa página principal, insira: 

    path('',include('*NOME_DO_APP*.urls'))
    
Com esse comando estamos redirecionando nossas URLs par as URLs que se encontram no nosso app.

Dentro da pasta do projeto vamos abrir o arquivo "settings.py" e adicionar dentro do array INSTALLED_APPS o nome do nosso aplicativo, aquele que foi criado através do comando startapp.

Agora podemos começar a criar nossas páginas web, para poder navegar entre diversas páginas dentro do web site, vamos precisar criar o path delas dentro da pasta do aplicativo nos arquivos urls.py e views.py. 
Começando pelas URLs, é necessario adicionar inicialmente esses código dentro do arquivo:

    from django.urls import path # gerenciador dos caminhos das páginas
    from . import views # chamando os arquivos que devem ser renderizados dentro das páginas
    
    urlpatterns = []




Explicar o projeto, se precisar relembrar algo ve o curso desse cara dnv: https://www.youtube.com/watch?v=A1nqCgAM6CE
relembrar UPDATE e DELETE: https://www.youtube.com/watch?v=EX6Tt-ZW0so&t=1259s

### Home Page
Dentro da página inicial do web site, temos duas opções que podem ser selecionadas:
    Add vulnerability: Adicionar uma nova vulnerabilidade
    Top 10 OWASP: Visualizar a tabela com todas vulnerabilidades registradas no banco de dados

### Register Page
