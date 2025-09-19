
from src.models.entities.music import Music
from src.models.repositories.musics_repository import musics_repository

class SongRegisterController:
    
    def insert(self, new_song_information: dict) -> dict:
        """
        Insere uma nova música após validar as informações e verificar duplicidade.

        Args:
            new_song_information (dict): Informações da música a ser cadastrada.

        Returns:
            dict: Resposta formatada indicando sucesso ou erro.
        """
        try:
            self.__verify_if_song_already_registered(new_song_information)
            self.__verify_songs_infos(new_song_information)
            self.__insert_song(new_song_information)
            return self.__format_response(new_song_information)
        except Exception as exception:
            return self.__format_error_response(exception)

    def __verify_if_song_already_registered(self, new_song_information: dict) -> None:
        """
        Verifica se a música já está cadastrada no sistema.

        Args:
            new_song_information (dict): Informações da música.

        Raises:
            Exception: Se a música já estiver cadastrada.
        """
        #interact with Model
        new_song_title = new_song_information["title"]
        search_response = musics_repository.find_music(new_song_title)

        if search_response is not None:
            raise Exception("Musica já cadastrada!")

    def __verify_songs_infos(self, new_song_information: dict) -> None:
        """
        Valida as informações da música, como título e ano.

        Args:
            new_song_information (dict): Informações da música.

        Raises:
            Exception: Se o título tiver mais de 100 caracteres ou o ano for inválido.
        """
        if len(new_song_information['title']) > 100:
            raise Exception("Titulo de musica com mais de 100 caracteres")
        
        year = int(new_song_information['year'])
        if year >= 2026:
            raise Exception("Ano de musica inválido!")

    def __insert_song(self, new_song_information: dict) -> None:
        """
        Insere a música no banco de dados ou sistema.

        Args:
            new_song_information (dict): Informações da música.
        """
        new_music = Music(
            title=new_song_information["title"],
            artist=new_song_information["artist"],
            year=int(new_song_information["year"])
        )
        musics_repository.insert_music(new_music)
    
    def __format_response(self, new_song_information: dict) -> dict:
        """
        Formata a resposta de sucesso após o cadastro da música.

        Args:
            new_song_information (dict): Informações da música.

        Returns:
            dict: Resposta de sucesso.
        """
        return {
            "success": True,
            "count": 1,
            "attributes": {
                "title": new_song_information["title"]
            }
        }
    
    def __format_error_response(self, err: Exception) -> dict:
        """
        Formata a resposta de erro em caso de exceção.

        Args:
            err (Exception): Exceção capturada.

        Returns:
            dict: Resposta de erro.
        """
        return {
            "success": False,
            "error": str(err)
        }