# Boas-vindas ao repositório do Spotnews

# Requisitos obrigatórios

Você acaba de entrar em um time responsável por criar um site de notícias usando o Django, considerando as suas habilidades com este framework, você recebeu tarefas para a construção de algumas partes do projeto, que representam  a base fundamental de todo o site. Segue o escopo de cada tarefa.:

## 1 - Crie a migrate e a model `Category`

local: `news/models.py`

> <b>🍀 Dica:</b> Os Requisitos 1 à 3 solicitarão a criação de modelos. Sempre que criar/modificar um modelo, é necessário criar as migrações para espelhar as modificações para os bancos de dados, inclusive o banco de testes contam com estas modificações. Comando para gerar a migrate a partir dos modelos criados:

```bash
python3 manage.py makemigrations
```

<details>
  <summary>
    <b>✍️ Detalhes do requisito</b>
  </summary>

* Crie a classe `Category`;
* A classe `Category` deve herdar os `models` do Django;
* A classe `Category` deve ter uma propriedade chamada `name`;
* A propriedade `name` deve ser um campo de caracteres com um tamanho máximo de **200 caracteres**;
* A propriedade `name` não deve aceitar informações vazias ou maiores que 200 caracteres;
* O método `__str__` da classe `Category` deve retornar a propriedade `name` da categoria criada;

</details>

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>

* Se a classe `Category` existe;
* Se a classe `Category` possui a propriedade `name`;
* Se é possível criar uma nova categoria;
* Se o método `__str__` retorna o nome da categoria criada;
* Se `name` possui uma propriedade de `max_length`;
* Se não é possível criar uma categoria com um nome vazio;
* Se não é possível criar uma categoria com um nome maior que 200 caracteres;
* Se as mensagens de validações são as padrões definidas pelo Django;

</details>

## 2 - Crie a migrate e a model `User`

local: `news/models.py`

<details>
  <summary>
    <b>✍️ Detalhes do requisito</b>
  </summary>

* Crie a classe `User`
* A classe `User` deve herdar os `models` do Django;
* A classe `User` deve ter as propriedades chamada `name`, `email`, `password` e `role`;
* As propriedades `name`, `password` e `role` devem ser campos de caracteres com um tamanho máximo de **200 caracteres**;
* A propriedade `email` deve ser um campo do tipo `email` com um tamanho máximo de **200 caracteres**;
* As propriedades devem ser:
  * `name`: Campo de caracteres, com tamanho máximo de **200 caracteres**;
  * `email`: Campo de email, , com tamanho máximo de **200 caracteres**;
  * `password`: Campo de caracteres, com tamanho máximo de **200 caracteres**;
  * `role`: Campo de caracteres, com tamanho máximo de **200 caracteres**;
* As propriedades `name`, `email`, `password` e `role` não devem aceitar informações vazias ou maiores que 200 caracteres;
* O método `__str__` da classe `User` deve retornar a propriedade `name` da pessoa usuária criada;

</details>

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>

* Se a classe `User` existe;
* Se a classe `User` possui as propriedades `name`, `email`, `password` e `role`;
* Se é possível criar uma nova pessoa usuária;
* Se o método `__str__` retorna o nome da pessoa usuária criada;
* Se `name`, `email`, `password` e `role` possuem uma propriedade de `max_length`;
* Se `name`, `password` e `role` são campos de caracteres;
* Se `email` é um campo de email;`
* Se não é possível criar uma pessoa usuária com alguma informação vazia;
* Se não é possível criar uma pessoa usuária com alguma informação maior que 200 caracteres;
* Se as mensagens de validações são as padrões definidas pelo Django;

</details>

## 3 - Crie a migrate e o model `News`

local: `news/models.py`

<details>
  <summary>
    <b>✍️ Detalhes do requisito</b>
  </summary>

* Crie a classe `News`;
* A classe `News` deve herdar os models do Django;
* A classe `News` deve ter as propriedades chamada `title`, `content`, `author`, `created_at`, `image` e `categories`;
* As propriedades devem ser:
  * `title`: Campo de caracteres com tamanho máximo de **200 caracteres** e com validação que não permita títulos com apenas uma palavra;
  * `content`: Campo de texto, sem tamanho máximo de caracteres;
  * `author`: Chave estrangeira da tabela ligada o model `User`;
  * `created_at`: Campo de data;
  * `image`: Campo de imagem;
  * `categories`: Chave estrangeira da tabela ligada o model `Category`;
* As propriedades `title`, `content`, `created_at` e `categories` não devem aceitar informações vazias;
* A propriedade `image` pode aceitar informações vazias;
* A propriedade `title` não deve aceitar informações maiores que 200 caracteres;
* A propriedade `created_at` não deve aceita datas fora do padrão `AAAA-MM-DD`;
* A propriedade `img` deve ter um campo `upload_to` que deve ser igual ao diretório `'img/'`;
* A propriedade `categories` deve aceitar 1 ou mais categorias e deve se relacionar como muitos para muitos;
* O método `__str__` da classe `News` deve retornar a propriedade `title` da notícia criada;

</details>

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>

* Se a classe `News` existe;
* Se é possível criar uma nova notícia;
* Se a classe `News` possui as propriedades `title`, `content`, `author`, `created_at`, `image` e `categories`;
* Se o método `__str__` retorna o título da notícia criada;
* Se não é possível criar uma notícia com alguma informação vazia;
* Se `title` possui uma propriedade de `max_length`;
* Se `content` não aceita informações menores que 1;
* Se ao tentar criar um notícia com alguma informação vazia, é gerada a resposta:

  ```sh
  {'<campo>': ['Este campo não pode estar vazio.']}
  ```

> Obs: substitua `<campo>` pelos campos `title` ou `content`.

* Se não é possível criar uma notícia com um título maior que 200 caracteres;
* Se ao tentar criar uma notícia com um título com uma única palavra, é gerada a seguinte resposta:
  
  ```sh
  'O título deve conter pelo menos 2 palavras.'.
  ```

  > Obs: você pode dar uma conferida [nessa página](https://docs.djangoproject.com/en/4.2/ref/forms/fields/#error-messages) da documentação sobre mensagens de erro personalizadas, ou perguntar para a IA da plataforma de aprendizagem.

</details>

---

> <b>🍀 Dica:</b> Antes de continuar, execute os 2 comandos abaixo:

```bash
python3 manage.py migrate
python3 manage.py runscript seeds
```
> O primeiro comando irá criar as tabelas no banco e o segundo comando irá popular o banco, execute um de cada vez

## 4 - Crie a página Inicial

local: news/templates/home.html

<details>
  <summary>
    <b>✍️ Detalhes do requisito</b>
  </summary>

* Crie um template para a página inicial do projeto;
* Crie a view e a url necessárias para renderizar o template `home.html`;
* Inclua as `urls` de `news` nas `urls` do projeto;
* O template da página inicial deve ser renderizado na rota `http://127.0.0.1:8000/`;
* O template deve ter uma tag `link` importando o arquivo css `css/style.css` que está na página de estáticos;
* A importação de arquivos estáticos deve ser feita através do template tag `static`;
* O caminho para a página inicial deve ter o nome de `home-page`;
* O template da página inicial deve ter como título `Página Inicial`;
* O template da página inicial deve ter um cabeçalho `header` com a classe `header`;
* O template da página inicial deve ter uma lista não ordenada com a classe `header-links` dentro do cabeçalho;
* O template da página inicial deve ter na lista não ordenada um link `a` com referência para a `home-page` e com o texto `Home`;
* O template da página inicial deve ter cards das notícias cadastradas no banco;
* O template da página inicial deve ter títulos `h2` com a classe `news-title` e os títulos das notícias como valores;
* O template da página inicial deve ter tags `span` com a classe `news-date` e a datas de criação das notícias como valores;
* O template deve exibir as datas no formato `DD/MM/AAAA`;
* O template da página inicial deve exibir as imagens das notícias;

</details>

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>

* Se existe uma url nomeada `home-page`;
* Se o template `home.html` está sendo renderizado na url `home-page`;
* Se existe uma importação do arquivo `static/css/style.css` como um `stylesheet`;
* Se existe um link para a `home-page` escrito `Home`;
* Se existe o título `Página Inicial`;
* Se existe um cabeçalho `header` com a classe `header`;
* Se existe uma lista não ordenada com a classe `header-links`;
* Se as notícias possuem um título `h2` com a classe `news-title`;
* Se as notícias possuem uma tag `span` com a classe `news-date` para a data;
* Se as datas das notícias estão no formato `DD/MM/AAAA`;
* Se as notícias possuem imagens;

</details>

> <b>🍀 Dica:</b> Algumas coisas nos próximos templates são parecidas com as do template criado agora, será que vale a pena pensar em um template base?

## 5 - Crie a página de Detalhes de uma Notícia

local: `news/templates/news_details.html`

<details>
  <summary>
    <b>✍️ Detalhes do requisito</b>
  </summary>

* Crie um template para a página detalhes da notícia;
* Crie a view e a url necessárias para renderizar o template `news_details.html`;
* O template da página detalhes da notícia deve ser renderizado na rota `http://127.0.0.1:8000/news/<int:id>`;

> Obs: o endpoint `<int:id>` deve ser substituído dinamicamente pelo id da notícia

* O caminho para a página detalhes da notícia deve ter o nome de `news-details-page`;
* O template da página detalhes da notícia deve ter como título `Página de Detalhes da Notícia`;
* O template da página detalhes da notícia deve ter um cabeçalho `header` com a classe `header`;
* O template da página detalhes da notícia deve ter uma lista não ordenada com a classe `header-links`;
* O template da página detalhes da notícia deve ter no cabeçalho um link `a` com referência para a `home-page` e com o texto `Home`;
* O template da página detalhes da notícia deve exibir as seguintes informações:
  * O título da notícia em título `h1`;
  * O conteúdo da notícia em parágrafo `p` com classe `news-content`;
  * Cada categoria da notícia em uma tag `span` com classe `news-categories`;
  * A pessoa autora da notícia em uma tag `span` com classe `news-author`;;
  * A imagem da notícia;
  * A data de criação da notícia no formato `DD/MM/AAAA`;
* Modifique as notícias no template `home.html` para que quando clicadas haja um redirecionamento para a página detalhes da notícia;

</details>

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>

* Se existe uma url nomeada `news-details-page`;
* Se o template `news_details.html` está sendo renderizado na url `news-details-page`;
* Se existe o título `Página de Detalhes da Notícia`;
* Se existe um cabeçalho `header` com a classe `header`;
* Se existe uma lista não ordenada com a classe `header-links`;
* Se a notícia possui um título em tag `h1` e com a classe `news-title`;
* Se a notícia possui um conteúdo em tag `p` e com a classe `news-content`;
* Se a notícia possui suas categorias em tags `span` e com a classe `news-categories`;
* Se a notícia possui uma pessoa autora em tag `span` e com a classe `news-author`;
* Se a notícia possui uma data e se esta data está no formato `DD/MM/AAAA`;
* Se a notícia possui imagem;

</details>

## 6 - Crie a página de Formulário de uma Nova Categoria

local: `news/templates/categories_form.html`

<details>
  <summary>
    <b>✍️ Detalhes do requisito</b>
  </summary>

* Crie um template para o formulário de cadastro de uma categoria;
* Crie a view e a url necessárias para renderizar o template `categories_form.html`;
* O template do formulário de uma nova categoria deve ser renderizado na rota `http://127.0.0.1:8000/categories/`;
* O caminho para o formulário de uma nova categoria deve ter o nome de `categories-form`;
* O template do formulário de uma nova categoria deve ter como título `Formulário para Nova Categoria`;
* O template do formulário de uma nova categoria deve ter um cabeçalho `header` com a classe `header`;
* O template do formulário de uma nova categoria deve ter uma lista não ordenada com a classe `header-links`;
* O template do formulário de uma nova categoria deve ter no cabeçalho um primeiro link `a` com referência para a `home-page` e com o texto `Home`;
* O template do formulário de uma nova categoria deve ter no cabeçalho um outro link `a` com referência para a `categories-form` e com o texto `Cadastrar Categorias`;
* O template do formulário de uma nova categoria deve ter uma tag de formulário com a propriedade `method` do tipo `post` e a propriedade `action` com a url para `/categories`;
* O template do formulário de uma nova categoria deve carregar o *token* de segurança `CSRF` em seu interior usando a tag de template adequada;
* O template do formulário de uma nova categoria deve ter uma `label` que como o valor `Nome`;
* O template do formulário de uma nova categoria deve ter um `input` com as algumas especificações:
  * A propriedade `type` do tipo `text`;
  * A propriedade `name` com o valor `name`;
  * A propriedade `maxlength` com o valor `200`;
  * Precisa ser um campo obrigatório;
* O template do formulário de uma nova categoria deve ter um botão do tipo `submit` com texto `Salvar`;
* Após o cadastro de uma categoria, a pessoa usuária deve ser redirecionada para a página principal;

</details>

 > <b>🍀 Dica:</b> Usar a criação de formulário nativa do Django pode agilizar as coisas

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>

* Se existe uma url nomeada `categories-form`;
* Se o template `categories_form.html` está sendo renderizado na url `categories-form`;
* Se existe o título `Formulário para Nova Categoria`;
* Se existe um cabeçalho `header` com a classe `header`;
* Se existe uma lista não ordenada com a classe `header-links`;
* Se existe um link para a `categories-form` escrito `Cadastrar Categorias`;
* Se existe a tag de formulário com as propriedades `method` e `action`;
* Se existe a tag `label`;
* Se existe a tag `input` com as propriedades `type`, `name`, `maxlength` e `required`;
* Se existe um botão do tipo `submit`;
* Se o formulário tem o estado inicial vazio;
* Se é possível cadastrar uma nova categoria;
* Se após o cadastro de uma nova categoria, há o redirecionamento para a página principal;

</details>

## 7 - Crie a página de Formulário de uma Nova Notícia

local: `news/templates/news_form.html`

<details>
  <summary>
    <b>✍️ Detalhes do requisito</b>
  </summary>

* Crie um template para o formulário de cadastro de uma notícia;
* Crie a view e a url necessárias para renderizar o template `news_form.html`;
* O template do formulário de uma nova notícia deve ser renderizado na rota `http://127.0.0.1:8000/news/`;
* O caminho para o formulário de uma nova notícia deve ter o nome de `news-form`;
* O template do formulário de uma nova notícia deve ter como título `Formulário para Nova Notícia`;
* O template do formulário de uma nova notícia deve ter um cabeçalho `header` com a classe `header`;
* O template do formulário de uma nova notícia deve ter uma lista não ordenada com a classe `header-links`;
* O template do formulário de uma nova notícia deve ter no cabeçalho um primeiro link `a` com referência para a `home-page` e com o texto `Home`;
* O template do formulário de uma nova notícia deve ter no cabeçalho um segundo link `a` com referência para a `categories-form` e com o texto `Cadastrar Categorias`;
* O template do formulário de uma nova notícia deve ter no cabeçalho um terceiro link `a` com referência para a `news-form` e com o texto `Cadastrar Notícias`;
* O template do formulário de uma nova notícia deve ter uma tag de formulário com a propriedade `method` do tipo `post`, a propriedade `action` com a url para `/news/` e a propriedade `enctype` com valor `multipart/form-data`;
* O template do formulário de uma nova notícia deve carregar o *token* de segurança `CSRF` em seu interior usando a tag de template adequada;
* O template do formulário de uma nova notícia deve ter as seguintes tag:
  * Uma `label` como o valor `Título`;
  * Um `input` do tipo `text` com o nome `title`;
  * Uma `label` como o valor `Conteúdo`;
  * Um `textarea` com o nome `content`;
  * Uma `label` como o valor `Autoria`;
  * Um `select` com o nome `author`;
  * Múltiplos `option` sendo seus valores os nomes das pessoas usuárias cadastradas no banco;
  * Uma `label` como o valor `Criado em`;
  * Um `input` do tipo `date` com o nome `created_at`;
  * Uma `label` como o valor `URL da Imagem`;
  * Um `input` do tipo `file` com o nome `image`;
  * Múltiplas `label` sendo seus valores os nomes das categorias cadastradas no banco;
  * Múltiplos `input` do tipo `checkbox` com o nome `categories`, cada input ligado a uma `label` de categoria;
  * Um botão do tipo `submit` com o valor `Salvar`;
  * Após o cadastro de uma notícia, a pessoa usuária deve ser redirecionada para a página principal;
</details>

> <b>🍀 Dica:</b> Lembre-se de que os arquivos vem em um local diferente do que os outros campos na requisição

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>

* Se existe uma url nomeada `news-form`;
* Se o template `news_form.html` está sendo renderizado na url `news-form`;
* Se existe o título `Formulário para Nova Notícia`;
* Se existe um cabeçalho `header` com a classe `header`;
* Se existe uma lista não ordenada com a classe `header-links`;
* * Se existe um link para a `home-page` escrito `Home`;
* Se existe um link para a `categories-form` escrito `Cadastrar Categorias`;
* Se existe um link para a `news-form` escrito `Cadastrar Notícias`;
* Se existe a tag de formulário com as propriedades `method` e `action`;
* Se existe a tag `label`;
* Se existe a tag `input` com as propriedades `type`, `name`, `maxlength` e `required`;
* Se existe a tag `label` como o valor `Título`;
* Se existe a tag `input` do tipo `text` com o nome `title`;
* Se existe a tag `label` como o valor `Conteúdo`;
* Se existe a tag `textarea` com o nome `content`;
* Se existe a tag `label` como o valor `Autoria`;
* Se existe a tag `select` com o nome `author`;
* Se existem as tags `option` sendo seus valores os nomes das pessoas usuárias cadastradas no banco;
* Se existe a tag `label` como o valor `Criado em`;
* Se existe a tag `input` do tipo `date` com o nome `created_at`;
* Se existe a tag `label` como o valor `URL da Imagem`;
* Se existe a tag `input` do tipo `file` com o nome `image`;
* Se existem as tags `label` sendo seus valores os nomes das categorias cadastradas no banco;
* Se existem as tags `input` do tipo `checkbox`;
* Se existe a tag botão do tipo `submit` com o valor `Salvar`;
* Se o formulário tem o estado inicial vazio;
* Se é possível cadastrar uma nova notícia;
* Se após o cadastro de uma nova categoria, há o redirecionamento para a página principal;

</details>

## 8 - Crie a rota `api/categories` com o DRF

locais: `news_rest/serializers/category_serializer.py` e `news_rest/views/category_view.py`

<details>
  <summary>
    <b>✍️ Detalhes do requisito</b>
  </summary>

* Adicione a rota `api/` nas urls do projeto;
* Vincule o `router` usado para construção da api com a rota `api/`do projeto;
* Registre no `router` a rotas `categories` com o `viewset` de `Category`;
* Crie um `serializer` que receba a model `Category` e tenha os campos `id` e `name`;
* Crie uma view que receba todas as categorias cadastradas no banco de dados e o `serializer` criado anteriormente;
* Crie uma rota para a view criada com o nome de `categories`;

</details>

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>

* Se existem os campos `id` e `name` no `serializer` de `Category`;
* Se os campos `id` e `name` apresentam os valores corretos;
* Se existe uma rota nomeada `api/categories`;
* Se a rota `api/categories` retorna todas as categorias cadastradas no banco de dados;
* Se é possível cadastrar uma nova categoria através da rota `api/categories`;
* Se é possível retornar a categoria criada através da rota `api/categories`

</details>

## 9 - Crie a rota `api/users` com o DRF

locais: `news_rest/serializers/user_serializer.py` e `news_rest/views/user_view.py`

<details>
  <summary>
    <b>✍️ Detalhes do requisito</b>
  </summary>

* Adicione a rota `api/` nas urls do projeto;
* Vincule o `router` usado para construção da api com a rota `api/`do projeto;
* Registre no `router` a rotas `users` com o `viewset` de `User`;
* Crie um `serializer` que receba a model `User` e tenha os campos `id`, `name`, `email` e `role`;
* Crie uma view que receba todas as pessoas usuárias cadastradas no banco de dados e o `serializer` criado anteriormente;
* Crie uma rota para a view criada com o nome de `users`;

</details>

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>

* Se existem os campos `id`, `name`, `email` e `role` no `serializer` de `User`;
* Se os campos `id`, `name`, `email` e `role` apresentam os valores corretos;
* Se o campo `password` não é retornado no `serializer` de `User`;
* Se existe uma rota nomeada `api/users`;
* Se a rota `api/users` retorna todos `users` cadastrados no banco de dados;
* Se é possível cadastrar um objeto `user` através da rota `api/users`;
* Se é possível retornar o objeto `user` criado através da rota `api/users`;

</details>

## 10 - Crie a rota `api/news` com o DRF

locais: `news_rest/serializers/news_serializer.py` e `news_rest/views/news_view.py`

<details>
  <summary>
    <b>✍️ Detalhes do requisito</b>
  </summary>

* Adicione a rota `api/` nas urls do projeto;
* Vincule o `router` usado para construção da api com a rota `api/`do projeto;
* Registre no `router` a rotas `news` com o `viewset` de `News`;
* Crie um `serializer` que receba a model `News` e tenha os campos `id`, `title`, `content`, `author`, `created_at`, `image` e `categories`;
* Crie uma view que receba todas as notícias cadastradas no banco de dados e o `serializer` criado anteriormente;
* Crie uma rota para a view criada com o nome de `news`;

</details>

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>

* Se existem os campos `id`, `title`, `content`, `author`, `created_at`, `image` e `categories` no `serializer` de `News`;
* Se os campos `id`, `title`, `content`, `author`, `created_at`, `image` e `categories` apresentam os valores corretos;
* Se existe uma rota nomeada `api/news`;
* Se a rota `api/news/` retorna todas as notícias cadastradas no banco de dados;
* Se é possível cadastrar uma nova notícia através da rota `api/news`;
* Se é possível retornar o objeto `news` criado através da rota `api/news`;
</details>

---
