from src.models.entities.music import Music
class __MusicRepository:
    """
    Uma classe para gerenciar um repositório (uma coleção) de músicas em memória.
    Esta classe funciona como um banco de dados temporário para o sistema.
    O prefixo de sublinhado duplo (__) indica que esta classe é para uso interno
    dentro deste módulo e não deve ser importada diretamente em outros lugares.
    """
    def __init__(self):
        """
        Inicializa o repositório de músicas.
        Cria
        """
        self.__music_list = []

    def insert_music(self, music:Music)->None:
        """
        Adiciona uma nova música à lista do repositório.

        Args:
            music (Music): Um objeto do tipo Music que será adicionado à lista.
        """
        self.__music_list.append(music)

    def find_music(self, music_title: str)->Music:
        """
        Busca uma música na lista pelo seu título.

        Args:
            music_title (str): O título da música a ser procurada.

        Returns:
            Music | None: O objeto Music correspondente se encontrado.
                          Caso contrário, retorna None.
        """
        for music in self.__music_list:
            if music.title == music_title:
                return music
        return None
            
    def get_all_songs(self)->list:
        """
        Retorna a lista completa de todas as músicas cadastradas no repositório.

        Returns:
            list[Music]: Uma lista contendo todos os objetos Music.
        """
        return self.__music_list


# Cria uma única instância (padrão Singleton - Design pattern) do repositório de músicas.
# Esta variável 'musics_repository' será importada por outras partes do
# programa para interagir com a lista de músicas.   
musics_repository = __MusicRepository()