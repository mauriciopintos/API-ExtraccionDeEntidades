# OpenIA.py
import openai
import json

def cargar_configuracion():
    try:
        with open('./app/OpenAI-config.json', 'r') as config_file:
            configuracion = json.load(config_file)
            return configuracion
    except FileNotFoundError:
        raise FileNotFoundError("El archivo OpenAI-config.json no se encuentra. Por favor, asegúrate de que existe y contiene la configuración necesaria.")

def configurar_openai():
    configuracion = cargar_configuracion()

    openai.api_type = "azure"
    openai.api_key = configuracion.get("api_key", "")
    openai.api_base = configuracion.get("api_base", "")
    openai.api_version = configuracion.get("api_version", "")

    return configuracion

def obtener_entidades_con_openai(texto):
    configuracion = configurar_openai()

    # Modelo de lenguaje GPT-3.5 Turbo
    model = "gpt-3.5-turbo"

    # Solicitud a la API de OpenAI para completar el chat
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": texto},
            {"role": "assistant", "content": 'Extract the following entities: names, emails, DNI numbers, license plates, credit card numbers, bank account numbers, phone numbers, addresses.'}
        ],
        deployment_id=configuracion.get("deployment_id", ""),
        temperature=0,
        max_tokens=150,  # Ajusta según sea necesario
        stop=None,
        n=1,
        stream=False
    )

    # Procesamiento de la respuesta
    salida = response['choices'][0]['message']['content']

    # Devuelve las entidades extraídas por OpenAI
    return {"extracciones_openai": salida}
