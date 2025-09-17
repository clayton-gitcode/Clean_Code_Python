
from src.view.song_register_view import SongRegisterView

def song_register_process():
    """
    Processa o registro de uma nova música.
    Esta função inicializa a visualização de registro de música, coleta as informações iniciais da música a ser registrada
    e prepara os dados para serem enviados ao controlador responsável pelo processamento do registro.
    Retorna:
        None
    """
    song_register_view = SongRegisterView()

    new_song_informations = song_register_view.registry_song_initial()
    # enviar new_song_informations para controller