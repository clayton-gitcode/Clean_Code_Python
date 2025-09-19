# Sistema de Gerenciamento Musical

Este projeto é uma aplicação de console desenvolvida em Python para gerenciar músicas e criar playlists. O sistema foi construído com foco em **Clean Code** e uma arquitetura organizada, separando as responsabilidades em diferentes camadas (Model, View, Controller).

## ✨ Funcionalidades

O sistema oferece as seguintes funcionalidades através de um menu interativo no terminal:

* **Cadastrar Música:** Permite que o usuário adicione uma nova música ao sistema, fornecendo título, artista e ano de publicação. O sistema valida os dados para evitar duplicidade e garantir a consistência das informações.
* **Criar Playlist:** Gera uma playlist aleatória a partir de todas as músicas cadastradas, embaralhando a ordem e exibindo a lista formatada para o usuário.
* **Sair:** Encerra a aplicação.

## 🏗️ Arquitetura do Projeto

O projeto segue um padrão de arquitetura inspirado no **MVC (Model-View-Controller)** para garantir um código limpo, organizado e de fácil manutenção:

* **Model:** Responsável pela representação dos dados e pela lógica de acesso a eles.
    * `src/models/entities/music.py`: Define a estrutura de uma música.
    * `src/models/repositories/musics_repository.py`: Simula um banco de dados em memória para armazenar, buscar e listar as músicas.

* **View:** Camada responsável pela interação com o usuário. Lida com toda a exibição de menus, solicitação de dados e formatação das respostas.
    * `src/view/first_view.py`: Exibe o menu principal.
    * `src/view/song_register_view.py`: Interface para o cadastro de músicas.
    * `src/view/playlist_creator_view.py`: Interface para a exibição da playlist.

* **Controller:** Contém a lógica de negócio da aplicação. Orquestra a comunicação entre a View e o Model.
    * `src/controllers/song_register_controller.py`: Valida e processa os dados para o cadastro de uma nova música.
    * `src/controllers/playlist_creator_controller.py`: Lida com a lógica de buscar as músicas e embaralhá-las.

* **Main (Orquestradores):** Responsável por inicializar a aplicação e conectar as camadas.
    * `src/main/process_handler.py`: Contém o loop principal que direciona o fluxo da aplicação com base na entrada do usuário.
    * `src/main/constructor/`: Arquivos que instanciam e conectam as Views e Controllers de cada funcionalidade.

## 🚀 Como Executar

1.  **Pré-requisitos:**
    * Certifique-se de ter o Python 3 instalado.

2.  **Execução:**
    * Navegue até o diretório raiz do projeto.
    * Execute o seguinte comando no seu terminal:

    ```bash
    python run.py
    ```
    * O menu principal será exibido, e você poderá interagir com o sistema digitando os comandos correspondentes.

## 📂 Estrutura de Arquivos

```
├── run.py                  # Ponto de entrada da aplicação
└── src/
    ├── controllers/        # Camada de controle (lógica de negócio)
    │   ├── playlist_creator_controller.py
    │   └── song_register_controller.py
    ├── main/
    │   ├── constructor/      # Orquestradores que conectam as camadas
    │   │   ├── playlist_creator_contructor.py
    │   │   └── song_register_contructor.py
    │   └── process_handler.py  # Gerenciador do fluxo principal
    ├── models/               # Camada de dados
    │   ├── entities/
    │   │   └── music.py
    │   └── repositories/
    │       └── musics_repository.py
    └── view/                 # Camada de apresentação (interface com usuário)
        ├── first_view.py
        ├── playlist_creator_view.py
        └── song_register_view.py
```
