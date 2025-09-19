import random
from src.models.repositories.musics_repository import musics_repository

class PlayListCreatorController:
    """
    Controlador responsável pela lógica de negócio para a criação de playlists.

    Esta classe orquestra o processo de buscar músicas no repositório,
    embaralhá-las para criar uma playlist aleatória e formatar a resposta
    para o cliente, seja de sucesso ou de erro.
    """

    def create_playlist(self) -> dict:
        """
        Orquestra a criação de uma playlist aleatória.

        Este é o método principal da classe, que chama métodos auxiliares para
        buscar as músicas, criar a playlist e formatar a resposta final.

        Returns:
            dict: Um dicionário contendo a playlist em caso de sucesso ou
                  uma mensagem de erro em caso de falha.
        """
        try:
            musics = self.__get_all_musics_and_verify()
            playlist = self.__create_playlist(musics)
            return self.__format_response(playlist)
        except Exception as exception:
            # Em caso de qualquer erro durante o processo, formata uma resposta de erro.
            return self.__format_error_response(exception)

    def __get_all_musics_and_verify(self) -> list:
        """
        Busca todas as músicas do repositório e verifica se a lista não está vazia.

        Raises:
            Exception: Lança uma exceção se nenhuma música for encontrada no repositório.

        Returns:
            list: Uma lista com todas as músicas registradas.
        """
        musics = musics_repository.get_all_songs()
        if not musics:  # Uma verificação mais "pythônica" para listas vazias
            raise Exception("Nenhuma música registrada!")
        return musics
    
    def __create_playlist(self, musics: list) -> list:
        """
        Cria uma playlist embaralhando uma lista de músicas.

        Args:
            musics (list): A lista de músicas a ser embaralhada.

        Returns:
            list: A mesma lista de músicas, porém com a ordem dos elementos aleatória.
        """
        random.shuffle(musics)
        return musics
    
    def __format_response(self, playlist: list) -> dict:
        """
        Formata a resposta HTTP para um cenário de sucesso.

        Args:
            playlist (list): A playlist criada e embaralhada.

        Returns:
            dict: Um dicionário padronizado para respostas de sucesso.
        """
        return {
            "success": True,
            "playlist": playlist,
        }
    
    def __format_error_response(self, err: Exception) -> dict:
        """
        Formata a resposta HTTP para um cenário de erro.

        Args:
            err (Exception): O objeto de exceção capturado.

        Returns:
            dict: Um dicionário padronizado contendo a mensagem de erro.
        """
        return {
            "success": False,
            "error": str(err)
        }