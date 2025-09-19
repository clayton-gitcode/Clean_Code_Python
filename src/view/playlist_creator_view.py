import os

class PlaylistCreatorView:
    """
    Responsável por exibir as informações da criação de playlists para o usuário.

    Esta classe lida com a interface do terminal (UI), mostrando mensagens
    de sucesso com os detalhes da playlist ou mensagens de erro formatadas.
    """

    def playlist_creator_success(self, controller_response: dict) -> None:
        """
        Exibe a playlist criada no terminal de forma formatada.

        Args:
            controller_response (dict): A resposta do controlador contendo
                a chave "playlist" com a lista de músicas.
        """
        self.__clear()
        print("✅ Playlist Criada com Sucesso! \n\n")

        for music in controller_response["playlist"]:
            # Usar f-strings torna a formatação mais limpa e legível.
            message = (
                f"   Título da música: {music.title}\n"
                f"   Artista: {music.artist}\n"
                f"   Ano de publicação: {music.year}\n"
                "   ----------------------------------"
            )
            print(message)

    def playlist_creator_fail(self, controller_response: dict) -> None:
        """
        Exibe uma mensagem de erro no terminal.

        Args:
            controller_response (dict): A resposta do controlador contendo
                a chave "error" com a descrição do erro.
        """
        self.__clear()
        message = (
            "❌ Erro na criação da playlist:\n\n"
            f"   * Motivo: {controller_response['error']}"
        )
        print(message)

    def __clear(self) -> None:
        """
        Limpa a tela do console.

        Este método privado executa o comando 'cls' (para Windows) ou 'clear'
        (para Linux/macOS) para limpar o terminal.
        """
        os.system("cls||clear")