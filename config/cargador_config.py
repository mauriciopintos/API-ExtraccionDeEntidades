# cargador_config.py
import json

def cargar_configuracion():
    try:
        with open('./config/OpenAI-config.json', 'r') as config_file:
            return json.load(config_file)
    except FileNotFoundError:
        raise FileNotFoundError("El archivo OpenAI-config.json no se encuentra. Por favor, asegúrate de que existe y contiene la configuración necesaria.")
