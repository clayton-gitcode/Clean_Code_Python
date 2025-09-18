
from src.view.song_register_view import SongRegisterView
from src.controllers.song_register_controller import SongRegisterController

def song_register_process():
    """
    Processa o registro de uma nova música.
    Esta função inicializa a visualização de registro de música, coleta as informações iniciais da música a ser registrada
    e prepara os dados para serem enviados ao controlador responsável pelo processamento do registro.
    Retorna:
        None
    """
    song_register_view = SongRegisterView()
    song_register_controller = SongRegisterController()

    new_song_informations = song_register_view.registry_song_initial()
    response = song_register_controller.insert(new_song_informations)

    if response["success"]:
        song_register_view.registry_song_success(response)
    else:
        song_register_view.regitry_song_fail(response)