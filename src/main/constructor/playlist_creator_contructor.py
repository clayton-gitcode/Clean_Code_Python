from src.view.playlist_creator_view import PlaylistCreatorView
from src.controllers.playlist_creator_controller import PlayListCreatorController

def playlist_creator_process() -> None:
    """Orquestra o processo de criação e exibição de uma playlist.

    Esta função atua como o "maestro" do caso de uso:
    1. Instancia a view, responsável pela interface com o usuário.
    2. Instancia o controller, responsável pela lógica de negócio.
    3. Chama o controller para executar a criação da playlist.
    4. Com base na resposta (sucesso ou falha), aciona o método
       correspondente na view para exibir o resultado final.
    """
    playlist_creator_view = PlaylistCreatorView()
    playlist_creator_controller = PlayListCreatorController()

    # Chama o controller e armazena a resposta (um dicionário)
    response = playlist_creator_controller.create_playlist()

    # Verifica o status da resposta e direciona para a view apropriada
    if response["success"]:
        playlist_creator_view.playlist_creator_success(response)
    else:
        playlist_creator_view.playlist_creator_fail(response)