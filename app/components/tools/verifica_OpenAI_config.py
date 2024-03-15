# validate_openai_credentials.py
import openai
import json

def cargar_configuracion():
    try:
        with open('./config/OpenAI-config.json', 'r') as config_file:
            return json.load(config_file)
    except FileNotFoundError:
        raise FileNotFoundError("El archivo OpenAI-config.json no se encuentra. Por favor, asegúrate de que existe y contiene la configuración necesaria.")

def validar_credenciales():
    configuracion = cargar_configuracion()
    openai.api_type = "azure"
    openai.api_key = configuracion.get("api_key", "")
    openai.api_base = configuracion.get("api_base", "")
    openai.api_version = configuracion.get("api_version", "")
    
    try:
        openai.ChatCompletion.create(
            model="text-davinci-003",
            messages=[
                {"role": "system", "content": "Este es un mensaje de prueba para validar las credenciales."},
                {"role": "user", "content": "Este es un mensaje de prueba para validar las credenciales."},
            ],
            deployment_id = configuracion.get("deployment_id", ""),
            temperature=0.8,
            max_tokens=150,
            stop=None,
            n=1,
            stream=False
        )
        print("Las credenciales de OpenAI son válidas.")
    except openai.error.AuthenticationError:
        print("Error: Las credenciales de OpenAI son inválidas.")

if __name__ == '__main__':
    validar_credenciales()
