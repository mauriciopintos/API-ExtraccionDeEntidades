# OpenAI_module.py
import openai
import json

def cargar_configuracion():
    try:
        with open('./config/OpenAI-config.json', 'r') as config_file:
            return json.load(config_file)
    except FileNotFoundError:
        raise FileNotFoundError("El archivo OpenAI-config.json no se encuentra. Por favor, asegúrate de que existe y contiene la configuración necesaria.")


def extraer_entidades_GPT(texto_json):
    # Almacenar los nombres del objeto JSON 
    nombres_propios = texto_json.get("nombres_propios", [])
    domicilios = texto_json.get("domicilios", [])
    
    # Lista para lmacenar los nombres validados por GPT
    nombres_gpt = []
    domicilios_gpt = []
    
    # Recorrer la lista de nombres
    for nombre in nombres_propios:
        
        if es_nombre_persona(nombre):
            nombre_limpio = limpia_nombre_persona(nombre)
            if es_nombre_persona(nombre_limpio):
                nombres_gpt.append(nombre_limpio)
    
    # Recorrer la lista de domicilios
    for domicilio in domicilios:
        domicilio_limpio = limpia_domicilio(domicilio)
        if domicilio_limpio != "ERROR":
            domicilios_gpt.append(domicilio_limpio)
            
    # Crear un nuevo JSON sin el campo "nombres_propios"
    salida_json = {}
    
    # Iterar sobre cada clave y valor del JSON original
    for key, value in texto_json.items():

        # Si la clave no es "nombres_propios", agregarla al nuevo JSON
        if key != "nombres_propios":
            if len(key) != 0:
                salida_json[key] = value
        
        # Si la clave no es "domicilios", agregarla al nuevo JSON
        if key != "domicilios":
            if len(key) != 0:
                salida_json[key] = value
    
    # Si la lista de nombres_propios no esta vacia agregarla a la salida_json
    if len(nombres_gpt) != 0:
        salida_json["nombres_propios"] = nombres_gpt
   
   # Si la lista de domicilios no esta vacia agregarla a la salida_json
    if len(domicilios_gpt) != 0:
        salida_json["domicilios"] = domicilios_gpt
        
    return salida_json


def es_nombre_persona(nombre):
    configuracion = cargar_configuracion()
    openai.api_type = "azure"
    openai.api_key = configuracion.get("api_key", "")
    openai.api_base = configuracion.get("api_base", "")
    openai.api_version = configuracion.get("api_version", "")
    
    # Preparar el texto de entrada para OpenAI
    prompt = f"¿'{nombre}' es un nombre de persona?"

    # Llamar a la API de OpenAI para verificar si el nombre es de una persona
    try:
        response = openai.ChatCompletion.create(
            model="text-davinci-003",
            deployment_id=configuracion.get("deployment_id", ""),
            messages=[
                {"role": "system", "content": "Eres un asistente útil especializado en la identificacion de nombres de personas."},
                {"role": "system", "content": f"cuando te pregunte si {prompt} solo vas a responder sí o no, ni una palabra más ni ménos, ningúna explicación, solo sí o no."},
                {"role": "system", "content": prompt}
            ],
            temperature=0.5,
            max_tokens=100,
            stop=None,
            n=1,
            stream=False
        )
        
        # Analizar la respuesta y determinar si el nombre se identifica como un nombre de persona
        if response.choices[0].message['content'].strip().lower() == 'sí.':
            return True
        else:
            return False
    except openai.error.AuthenticationError:
        print("Error: Las credenciales de OpenAI son inválidas.")
        return False


def limpia_nombre_persona(nombre):
    configuracion = cargar_configuracion()
    openai.api_type = "azure"
    openai.api_key = configuracion.get("api_key", "")
    openai.api_base = configuracion.get("api_base", "")
    openai.api_version = configuracion.get("api_version", "")
    
    # Preparar el texto de entrada para OpenAI
    prompt = f"'Retornar SOLAMENTE el nombre/s y/o apellido/s de persona, ya sea que el texto contenga nombre, nombres, apellido, apellidos y/o cualquiera de las combinaciones, SIN NINGUN TEXTO ADICIONAL, del texto:{nombre}'"
    valores_invalidos = "Garantías, Recurso, Casación, Cámara, Apelación, Concédase, Autos"
    
    # Llamar a la API de OpenAI para limpiar el nombre es de una persona
    try:
        response = openai.ChatCompletion.create(
            model="text-davinci-003",
            deployment_id=configuracion.get("deployment_id", ""),
            messages=[
                {"role": "system", "content": "Eres un asistente útil especializado en la extracción de nombres y apellidos de personas de un texto dado."},
                {"role": "system", "content": f"Considerá que un nombre de persona puede estar compuesto por uno varios nombres y/o uno o varios apellidos."},
                {"role": "system", "content": f"Considerá que un nombre de persona puede estar compuesto por solo un nombre."},
                {"role": "system", "content": f"Considerá que un nombre de persona puede estar compuesto por solo un apellido."},
                {"role": "system", "content": f"Si recibis una sola palabra debes considerarla como nombre de persona."},
                {"role": "system", "content": f"Si recibis un valor que no podes identificar como un nombre o un apellido, devolvé solamente la palabra 'ERROR'sin explicar nada más."},
                {"role": "system", "content": f"'Si recibis en el texto:{nombre}, un valor como {valores_invalidos}, no debes incluirlo como parte de la respuesta.'"},
                {"role": "system", "content": f"'Cuando te solicite: {prompt} solo vas a responder con lo requerido, ni una palabra más ni ménos, ningúna explicación, solo lo estrictamente requerido, sin un punto al final.'"},
                {"role": "system", "content": prompt}
            ],
            temperature=0.5,
            max_tokens=100,
            stop=None,
            n=1,
            stream=False
        )
        
        # Procesar la respuesta para extraer el nombre de persona limpio
        nombre_limpio = response.choices[0].message['content'].strip()
        return nombre_limpio
        
    except openai.error.AuthenticationError:
        print("Error: Las credenciales de OpenAI son inválidas.")
        return False

def limpia_domicilio(domicilio):
    configuracion = cargar_configuracion()
    openai.api_type = "azure"
    openai.api_key = configuracion.get("api_key", "")
    openai.api_base = configuracion.get("api_base", "")
    openai.api_version = configuracion.get("api_version", "")
    
    # Preparar el texto de entrada para OpenAI
    tipo_buscado = "Domicilio, Barrio, Ciudad, Pueblo, Locación, Localidad, Ruta, Calle, Avenida, Av., Cra., Carrera, Carretera, Pasaje, Pje., Paraje, Villa, Estancia, Comarca, Plaza, Pza.,Plz., Camino, Cd., Col., Colonia"
    prompt = f"'Retornar SOLAMENTE los datos que correspondan con {tipo_buscado}, SIN NINGUN TEXTO ADICIONAL, del texto:{domicilio}'"

    # Llamar a la API de OpenAI para limpiar el nombre es de una persona
    try:
        response = openai.ChatCompletion.create(
            model="text-davinci-003",
            deployment_id=configuracion.get("deployment_id", ""),
            messages=[
                {"role": "system", "content": "Eres un asistente útil especializado en la identificacion de dimicilios, barrios, locaciones y localidades."},
                {"role": "system", "content": f"'Si recibis algun texto que no podes identificar como un {tipo_buscado}, devolvé solamente la palabra 'ERROR' sin explicar nada más.'"},
                {"role": "system", "content": f"Cuando te solicite: {prompt} solo vas a responder con lo requerido, ni una palabra más ni ménos, ningúna explicación, solo lo estrictamente requerido, sin un punto al final."},
                {"role": "system", "content": prompt}
            ],
            temperature=0.5,
            max_tokens=100,
            stop=None,
            n=1,
            stream=False
        )
        
        # Procesar la respuesta para extraer el domicilio limpio
        domicilio_limpio = response.choices[0].message['content'].strip()
        return domicilio_limpio
        
    except openai.error.AuthenticationError:
        print("Error: Las credenciales de OpenAI son inválidas.")
        return False

