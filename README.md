# Ferramentas utilizadas
Web application desenvolvida com Python utilizando Django como back-end, Bootstrap e CSS inline utilizado no front-end da aplicação, banco de dados utilizado em sqlite3 e a SGDB escolhida foi o Django Administration.

# Introdução
Essa aplicação web tem como intuito gerenciar as vulnerabilidades do top 10 OWASP, permitindo que o usuário realize as funções de um CRUD (criar, ler, editar e deletar). 

Para adicionar uma nova vulnerabilidade, basta enviar um formulário na página de registro, que após validado será adicionado como um novo objeto no banco de dados. 
Existe uma página específica para visualização das vulnerabilidades registradas no banco de dados em formato de tabela, onde elas podem ser alteradas ou excluídas via ícones específicos, atendendo as regras do CRUD.

# Let's Start
## Criação do projeto
Para iniciar é necessário que as ferramentas Python e alguma IDE de sua preferência (VSCode ou Sublime são recomendados) estejam instalados. 
Após instalado o Python é necessário instalar a biblioteca Django utilizando o comando: "python -m pip install Django". Através da Internet baixar o Bootstrap e copiar a pasta static para dentro do projeto.

Após a instalação das ferramentas criar um diretório para a web Application e executar dentro dele o seguinte comando do Django para iniciar o projeto:
 
    python -m django startproject *NOME_DO_PROJETO*

Agora criar o aplicativo que é o responsável pelas configurações do back-end e do banco de dados utilizando o seguinte comando:

    python manage.py startapp *NOME_DO_APP*

# Configuração do projeto
Abrir o arquivo "urls.py" que está na pasta do projeto (esse arquivo manipula as URLs), dentro do array urlpatterns adicione o seguinte path da página principal para criar o redirecionamento para as URLs que se encontram no app.

    path('',include('*NOME_DO_APP*.urls'))

Dentro da pasta do projeto, abrir o arquivo "settings.py" e adicionar no array INSTALLED_APPS o nome do aplicativo.

Agora pode-se criar as páginas web, é necessário criar o path delas dentro da pasta do aplicativo nos arquivos urls.py e views.py, mas antes de prosseguir com a linkagem do path com as views, crie uma pasta templates dentro do diretório do aplicativo, esse diretório será responsável por armazenar os arquivos .html, que são as páginas do website, criar inicialmente um novo arquivo chamado "home.html" dentro do diretório templates.

Começando a configuração das URLs, adicionar os seguintes códigos dentro do arquivo urls.py:

    from django.urls import path # gerenciador dos caminhos das páginas
    from . import views # chamando os arquivos que devem ser renderizados dentro das páginas
    
    urlpatterns = []

Seguir para o array "urlpatterns" adicionar o path da página, a “def” e o nome único de identificação, utilizando o comando abaixo:

    urlpatterns = [
        path('', views.home, name="home")
    ]

Dentro do arquivo "views.py", importar o render da biblioteca do Django, configurar o TEMPLATE_DIRS utilizando o script abaixo:

    from django.shortcuts import render

    TEMPLATE_DIRS = ('os.path.join(BASE_DIR, "templates")')


Agora sim criar a "def" dentro do arquivo views.py para renderizar o arquivo "home.html" utilizando o script abaixo:

    def home(request):
        return render(request, 'home.html',{})

Para iniciar a aplicação, dentro do console insira o seguinte comando:

    python manage.py runserver

Será exibido no console o link da aplicação, ex.: "http://127.0.0.1:8000/".

Seguindo a mesma lógica de criação do path com a renderização de páginas pela “def” pode-se criar quantas páginas forem necessárias dentro da aplicação! Segue exemplo para adicionar uma outra página:

Dentro do urls.py:

    urlpatterns = [
        path('', views.home, name="home"),
        path('/conteudo', views.content, name="content")
    ]

Dentro da views.py:

    def content(request):
        return render(request, 'content.html',{})

com esses scripts é possível acessar a home page (ex.: "http://127.0.0.1:8000/") e a página de conteúdos (ex.: "http://127.0.0.1:8000/conteudo").

# Estrutura do projeto
## Home Page
Dentro da página inicial existem duas opções de seleção:
 *Add vulnerability: Para adicionar uma nova vulnerabilidade.
 *Top OWASP: Para visualizar a tabela com todas as vulnerabilidades registradas no banco de dados.

## Add vulnerability Page
Será exibido um formulário para enviar uma requisição através do método POST para o banco de dados.

Preencher corretamente todos os campos do formulário, será exibido um aviso no campo que conter algum erro e será impedido o envio de um formulário até que seja corrigido. Após a validação dos campos será exibido um alerta para conferencia dos dados do formulário e um novo objeto é inserido no banco de dados.

Função create do objetivo CRUD.

## Top OWASP Page
Essa é a página de visualização dos itens registrados no banco de dados em formato de tabela. Não foi restringido a "Top 10" para que fosse possível adicionar quantas vulnerabilidades forem necessárias. Os registros estão organizados pelo código e ano, podendo assim comparar versões mais recentes e antigas.

Função read do objetivo CRUD.

Observação: Na coluna “edit” e “delete” existem dois ícones (lápis e X) que redireciona respectivamente para a página de edição e exclusão do objeto no banco de dados.

## Update Page
Nessa página é possível editar o objeto. Pelo ID passado pela URL é identificado o objeto selecionado na tabela.

Uma vez selecionado é exibido mesmo o formulário da página de registro, porém com todos os campos preenchidos, basta selecionar o campo desejar para editar.
Por utilizar o mesmo arquivo HTML da página de registro, através de um trigger (que é acionado quando o path da página contém "update") o título e o texto do botão serão alterados.

As alterações passarão pelo mesmo processo de validação do formulário de registro, e qualquer erro será sinalizado. Função update do objetivo CRUD.

## Delete Page
A página de exclusão permite deletar um objeto selecionado na tabela do banco de dados. É utilizada a mesma lógica do ID passado pela URL para identificar o objeto selecionado.

Antes de consolidar a exclusão é solicitada uma confirmação para evitar equívoco. Na confirmação são exibidos o código, título e ano do objeto que será deletado. Se todas as informações estiverem corretas, clicar no botão "Confirm" para excluir o objeto do banco de dados.

Função delete do objetivo CRUD.
