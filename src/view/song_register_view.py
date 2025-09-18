import os
class SongRegisterView:
    """
    Classe responsável pela interface de registro de músicas.
    Métodos
    -------
    registry_song_initial() -> dict
        Solicita ao usuário as informações de uma nova música (título, artista e ano de publicação)
        e retorna um dicionário contendo esses dados.
    """
    def registry_song_initial(self)->dict:

        self.__clear()
        print("Implementar nova Musica \n\n")

        title = input("Nome da musica: ")
        artist = input("Nome do artista: ")
        year = input("ano de puclicacao: ")

        new_song_informations={
            "title": title, "artist": artist, "year":year
        }

        return new_song_informations

    def registry_song_success(self, controller_response: dict)->None:
        self.__clear()
        message = '''
            Musica cadastrada com sucesso!

            * Titulo: {}
            * Quantidade: {}
        '''.format(
                controller_response["attributes"]["title"],
                controller_response["count"]
            )
        print(message)

    def regitry_song_fail(self, controller_response: dict)->None:
        self.__clear()
        message = '''
            Falha ao registrar musica

            *Erro: {}
        '''.format(controller_response["error"])
        print(message)

    def __clear(self):
        os.system("cls||clear")