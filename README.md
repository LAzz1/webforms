# Ferramentas utilizadas
Web application desenvolvida com Python utilizando Django como back-end, Bootstrap e CSS inline utilizado no front-end da aplicação, banco de dados utilizado em sqlite3 e a SGDB escolhida foi o Django Administration.
 
# Introdução
Essa aplicação web tem como intuito gerenciar as vulnerabilidades do top 10 OWASP, permitindo que o usuário realize as funções de um CRUD (criar, ler, editar e deletar). Para adicionar uma nova vulnerabilidade, basta enviar um formulário na página de registro, que caso passe por todas validações, será adicionado um novo objeto no banco de dados, para visualizar as vulnerabilidades registradas, é necessário ir para página de visualização, na qual é exibida uma tabela com todos os itens do nosso banco de dados, dentro desta tabela já temos um link para as outras duas opções do CRUD, editar e deletar.
 
Ao clicar no ícone de lápis vai haver o redirecionamento para um formulário de edição do objeto selecionado na tabela. Entretanto, clicando no ícone de "X", será redirecionado para a página de exclusão da vulnerabilidade selecionada.
 
# Let's Start
## Criação do projeto
Primeiramente será necessário instalar as ferramentas utilizadas no projeto, Python e uma IDE de sua preferência (VSCode ou Sublime são recomendados). Após instalar o Python, baixe e instale o Django através do comando "python -m pip install Django". Para a utilização do Bootstrap deve-se baixar a pasta static que contém o nosso Bootstrap para ser utilizado no estilo da nossa página.
 
Após a instalação das ferramentas será necessário criar um projeto para nossa web application, crie um diretório para armazenar seu projeto e rode dentro dela o seguinte comando para criar um projeto do Django:
 
    python -m django startproject *NOME_DO_PROJETO*
   
Em seguida crie o seu aplicativo, que é o responsável pelas configurações do back-end e banco de dados, basta continuar no diretório criado para armazenar todo o projeto e rodar o seguinte comando:
 
    python manage.py startapp *NOME_DO_APP*
   
## Configuração do projeto
Seguindo para a configuração do projeto, vá dentro da pasta do projeto (a que criamos com o primeiro comando) e abra o arquivo "urls.py", com esse arquivo pode-se manipular as URLs que estarão no site. Dentro do array urlpatterns adicione o path da página principal:
 
    path('',include('*NOME_DO_APP*.urls'))
   
Com esse comando será criado um redirecionamento para as URLs que se encontram no app.
 
Dentro da pasta do projeto em "settings.py", adicione dentro do array INSTALLED_APPS o nome do nosso aplicativo.
 
Agora é pode-se criar as páginas web, é necessário criar o path delas dentro da pasta do aplicativo nos arquivos urls.py e views.py, mas antes de prosseguir com a linkagem do path com as views, crie uma pasta templates dentro do diretório do aplicativo, esse diretório será responsável por armazenar os arquivos .html, que nada mais são que nossas páginas do website, crie inicialmente um novo arquivo chamado "home.html" dentro do diretório templates.
 
Começando pelas URLs, é necessário adicionar inicialmente esses código dentro do arquivo:
 
    from django.urls import path # gerenciador dos caminhos das páginas
    from . import views # chamando os arquivos que devem ser renderizados dentro das páginas
   
    urlpatterns = []
 
agora dentro do array "urlpatterns" adicione o path da nossa página, chame a def que ainda não foi criada, mas será no próximo passo e por último de um nome único para esse path. O array urlpatterns deve ficar da seguinte maneira:
 
    urlpatterns = [
        path('', views.home, name="home")
    ]
 
Com o path criado, vá criar agora a "def" dentro do arquivo views.py que vai renderizar nosso arquivo "home.html" dentro do path que foi definido no passo anterior, (pode-se criar as views primeiro e depois definir os paths, a ordem não altera o resultado) dentro do "views.py" as "def" para renderizar os arquivos devem retornar o arquivo que desejamos renderizar, e para isso será necessário importar a função "render" do Django dentro do arquivo, já para os arquivos HTML serem encontrados, é necessário a inclusão deles no TEMPLATE_DIRS. Segue como o arquivo "views.py" deve ficar:
   
    from django.shortcuts import render
   
    TEMPLATE_DIRS = ('os.path.join(BASE_DIR, "templates")')
   
    def home(request):
        return render(request, 'home.html',{})
 
Agora é possível iniciar nossa aplicação! Dentro do console insira o comando:
   
    python manage.py runserver
 
vai ser exibido no console o link da sua aplicação, que deve vir como um ip, "http://127.0.0.1:8000/".
 
Seguindo essa lógica de criação dos path com a renderização das páginas podemos criar quantas páginas forem necessárias para nossa aplicação! Um último exemplo de como adicionar uma outra página:
 
Dentro do urls.py:
 
    urlpatterns = [
        path('', views.home, name="home"),
        path('/conteudo', views.content, name="content")
    ]
   
Dentro da views.py:
       
    def content(request):
        return render(request, 'content.html',{})
 
 com essas definições é possível acessar a home page no link exemplo "http://127.0.0.1:8000/" e a página de conteúdos no link "http://127.0.0.1:8000/conteudo".
 
# Estrutura do projeto
## Home Page
Dentro da página inicial do web site, existem duas opções que podem ser selecionadas:
    Add vulnerability: Adicionar uma nova vulnerabilidade
    Top OWASP: Visualizar a tabela com todas vulnerabilidades registradas no banco de dados
 
## Add vulnerability Page
Na página de registro de uma nova vulnerabilidade pode-se observar um formulário, através deste formulário é possível enviar uma requisição através do método POST para o nosso banco de dados.
 
Ao tentar enviar o formulário sem preencher nenhum dos campos ou com algum erro, vão ser exibidas mensagens de erro que impediram o envio de um formulário errado ao banco de dados, após preencher todos os campos corretamente e enviar o formulário, é exibido um alerta para prevenir o usuário de registrar um objeto errado, no qual exibe todas informações do formulário para uma revisão das informações. Com todas as informações e validações corretas um novo objeto é inserido no banco de dados.
 
Com o objetivo de criar um CRUD, já foi realizada a função de Criar.
 
## Top OWASP Page
Essa é a página de visualização dos itens registrados no nosso banco de dados, inicialmente deveria ser um "Top 10", porém para não se restringir a apenas 10 vulnerabilidades foi deixado livre para adicionar quantas forem necessárias, é muito interessante deixar livre para comparar o "Top 10" atual com suas versões anteriores, como o "Top 10" de 2017, dentro da tabela organizei por código e ano, assim podemos ter as versões mais recentes e antigas uma do lado da outra. Concluído a função de Ler do CRUD.
 
Observando a coluna de “edit” e “delete”, encontra-se dois ícones, um lápis que nos redireciona para a página de edição dos objetos do nosso banco de dados e o ícone de "X", que nos redireciona para a página de excluir objetos.
 
## Update Page
Nessa página é passado o ID do objeto do banco de dados pela URL para podermos editar o objeto que realizamos o clique dentro da tabela de visualização. Dentro da página é exibido o mesmo formulário da página de registro, porém ele vem preenchido com as informações do objeto selecionado para a edição poder ser realizada mais facilmente, por utilizar o mesmo arquivo HTML da página de registro, foi utilizado um trigger para quando o path da página contém "update" o título e o texto do botão serão mudados.
 
Esse formulário funciona exatamente da mesma forma que o de registro, com os campos todos preenchidos corretamente, validações feitas sem apresentar erros e concordando com o alerta de prevenção de erros, o objeto selecionado tem seus parâmetros editados. Função de update do CRUD realizada.
 
## Delete Page
A última função do nosso CRUD pode ser realizada dentro da página de exclusão, nela vamos poder deletar os objetos selecionados na tabela do banco de dados.
 
É utilizada a mesma lógica dos IDs dos objetos passados pela URL para sabermos qual objeto deve ser deletado, nesta página é feita uma confirmação para o usuário evitar excluir o objeto errado, é exibido na tela o código, título e ano da vulnerabilidade que será deletada. No caso de todas as informações estarem corretas basta clicar no botão escrito "Confirm" para deletar o objeto do banco de dados.