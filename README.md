# Ferramentas utilizadas
Web aplication desenvolvida com Python utilizando Django como back-end, Bootstrap e CSS inline utilizado no front-end da aplicação, o banco de dados utilizado foi o sqlite3 e a SGDB escolhida foi o Django Administration.

# Introdução
Essa aplicação web tem como intuito gerenciar as vulnerabilidades do top 10 OWASP, permitindo que o usuario realize as funções de um CRUD (criar, ler, editar e deletar). Para adicionar uma nova vulnerabilidade, basta enviar um formulário na página de registro, que caso passe por todas validações, será adicionado um novo objeto no banco de dados, para visualizar as vulnerabilidades registradas, devemos ir para página de visualização, na qual é exibida uma tabela com todos os items do nosso banco de dados, dentro dessa tabela já temos um link para as outras duas opções do CRUD, editar e deletar. 

Clicando no icone de lápis vamos ser redirecionado para um formulário de edição do objeto selecionado na tabela. Entretando se clicarmos no icone de "X", vamos ser redirecionados para a página de exclusão da vulnerabilidade selecionada.

# Let's Start
## Criação do projeto
Primeiramente vamos precisar instalar as ferramentas utilizadas no projetos, será necessario instalar o Python e uma IDE de sua preferencia (recomendo VSCode ou Sublime), após instalar o python será necessário baixar e instalar o Django através do comando "pip" do Python. Para a utilização do Bootstrap deve-se baixar a pasta static que contem o nosso Bootstrap para ser utilizado no estilo da nossa página.

Após a instalação das ferramentas será necessário criar um projeto para nossa web aplication, crie uma diretório para armazenar seu projeto e rode dentro dela o comando: 

    django-admin.py startproject *NOME_DO_PROJETO*
    
Em seguida vamos criar o nosso aplicativo, que é o responsavel pelas configurações do back-end e banco de dados, basta continuar no diretório criado para armazenar todo o projeto e rodar o seguinte comando:

    python manage.py startapp *NOME_DO_APP*
    
## Configuração do projeto
Seguindo para a configuração do nosso projeto, devemos ir dentro da pasta do projeto (a que criamos com o primeiro comando) e abrir o arquivo "urls.py", com esse arquivo podemos manipular as URLs que estaram no nosso site. Dentro do array urlpatterns adicione outro path da nossa página principal, insira: 

    path('',include('*NOME_DO_APP*.urls'))
    
Com esse comando estamos redirecionando nossas URLs par as URLs que se encontram no nosso app.

Dentro da pasta do projeto vamos abrir o arquivo "settings.py" e adicionar dentro do array INSTALLED_APPS o nome do nosso aplicativo, o mesmo que foi criado através do comando startapp.

Agora podemos começar a criar nossas páginas web, vamos precisar criar o path delas dentro da pasta do aplicativo nos arquivos urls.py e views.py, mas antes de prosseguirmos com a linkagem do path com as views, devemos criar uma pasta templates dentro do diretório do nosso aplicativo e dentro dela colocar todos arquivos.html que futuramente vão ser nosssas páginas web. Então após criar a pasta templates crie dentro dela o arquivo "home.html".

Começando pelas URLs, é necessario adicionar inicialmente esses código dentro do arquivo:

    from django.urls import path # gerenciador dos caminhos das páginas
    from . import views # chamando os arquivos que devem ser renderizados dentro das páginas
    
    urlpatterns = []

agora dentro do array "urlpatterns" podemos adicionar o path da nossa página, chamar a def que furturamente será criada dentro do arquivo "views.py" e por ultimo dar um nome unico para esse path. Ficaria da seguite maneira uma home page:

    urlpatterns = [
        path('', views.home, name="home")
    ]
 
Com nosso path criado, devemos criar a "def" dentro do arquivo views.py que vai renderizar nossa página dentro desse caminho (podemos criar as views primeiro e depois definir os paths, a ordem não altera o resultado), dentro da views.py as "def" para renderizar os arquivos devem retornar o arquivo que desejamos renderizar no respectivo path e para isso sera necessário importar a função "render" do Django dentro do arquivo. Segue como o arquivo deve ficar:
    
    from django.shortcuts import render
    
    def home(request):
        return render(request, 'home.html',{})

Podemos agora iniciar nossa aplicação! Dentro do console insira esse comando:
    
    python manage.py runserver

vai ser exibido no console o link da sua aplicação, que deve vir como um ip, "http://127.0.0.1:8000/". Seguindo essa lógica de criação dos path com a renderização das páginas podemos criar quantas páginas forem necessaria para nossa aplicação! Um ultimo exemplo de uma página adicional:

Dentro do urls.py:

    urlpatterns = [
        path('', views.home, name="home"),
        path('/conteudo', views.content, name="content")
    ]
    
Dentro da views.py:
    
    from django.shortcuts import render
    
    def home(request):
        return render(request, 'home.html',{})
    
    def content(request):
        return render(request, 'content.html',{})
 
 com essas definições é possivel acessar a home page no link exemplo "http://127.0.0.1:8000/" e a página de conteudos no link "http://127.0.0.1:8000/conteudo".

# Estrutura do projeto
## Home Page
Dentro da página inicial do web site, temos duas opções que podem ser selecionadas:
    Add vulnerability: Adicionar uma nova vulnerabilidade
    Top OWASP: Visualizar a tabela com todas vulnerabilidades registradas no banco de dados

## Add vulnerability Page
Na página de registro de uma nova vulnerabilidade podese observar um formulário, através desse formulário que vamos enviar uma requisição através do método POST para o nosso banco de dados.

Ao tentar enviar o formulário sem preencher nenhum dos campos, vão ser exibidas mensagens de erro que impediram o envio de um formulário contendo erros, após preencher todos os campos corretamente e enviar o formulário, é exibido um alerta para prevenir o usuario de registrar um objeto errado, no qual exibe todas informações do formulário para uma revisão das informações. Com todas informações e validações corretar um novo objeto é inserido no banco de dados. 

Com o objetivo de criar um CRUD, já realizamos a função de Criar.

## Top OWASP Page
Essa página é a página de visualização dos items registrados no nosso banco de dados, inicialmente deveria ser um "Top 10", porém para não se restrigir a apenas 10 vulnerabilidades deixei livre para adicionar quantas forem necessarias, é muito interessante deixar livre caso seja adicionado o "Top 10" de 2017, dentro de uma tabela podemos visualizar o "Top 10" antigo com o mais rescente. Concluido a função de Ler do CRUD.

Observando a coluda de edit e delete, temos dois icones, um lápis que nos leva para página de edição dos objetos do nosso banco de dados e o icone de "X", que nos leva para página de excluir objetos.

## Update Page
Nessa página é passado o ID do objeto do banco de dados pela URL para podermos editar o objeto que realizamos o clique dentro da tabela de visualização. Dentro da página é exibido o mesmo formulário da página de registro, porem ele vem preenchido com as informações do objeto selecionado para a edição poder ser realizada mais facilmente, além dessa mudança temos a do titulo e a do texto do botão, realizadas através de um trigger quando a URL da página contem "update".

Esse formulário funciona exatamente da mesma forque que o de registro, com os campos todos preenchidos corretamente, validações feitas sem apresentar erros e concordando com o alerta de prevenção de erros, o objeto selecionado tem seus parametros editados.

## Delete Page
A ultima função do nosso CRUD pode ser realizada dentro dessa página, nela vamos poder deletar os objetos selecionados na tabela do banco de dados.

É utilizada a mesma lógica dos IDs dos objetos passados pela URL para sabermos qual objeto deve ser deletado, nessa página é feita uma confirmação para o usuario evitar excluir o objeto errado, é exibido na tela o código, titulo e ano da vulnerabilidade que sera deletada. No caso de todas informações estarem corretas basta clicar no botão escrito "Confirm" para deletar o objeto do banco de dados.
