# decode_escapado_module.py
import json
from flask import Response

def decodificar_json_escapado(json_string):
# def decodificar_json_escapado(data):

    # Si ya viene un diccionario en lugar de una cadena JSON, conviértelo en una cadena JSON
    if isinstance(json_string, dict):
        json_string = json.dumps(json_string)
    
    # Carga la cadena JSON
    data = json.loads(json_string)

    # Itera sobre los elementos del diccionario
    for key, value in data.items():
        # Si el valor es una lista, itera sobre los elementos de la lista
        if isinstance(value, list):
            # Reemplaza cada elemento de la lista con su versión decodificada
            data[key] = [item.encode().decode('unicode_escape') for item in value]
        else:
            # De lo contrario, simplemente decodifica el valor
            data[key] = value.encode().decode('unicode_escape')

    # Devuelve los datos decodificados
    return data
