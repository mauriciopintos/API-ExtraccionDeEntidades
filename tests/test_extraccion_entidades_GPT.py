# test_extraccion_entidades_GPT.py
import os
import subprocess
import time
from decode_escapado_test import decodificar_texto_escapado

def procesar_archivos_seleccionados(ruta_curl, numeros_archivos):
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    carpeta_salida = f"{directorio_actual}/textos/entidades"
    
    # Verificar si la carpeta de salida ya existe
    if not os.path.exists(carpeta_salida):
        # Crear la carpeta si no existe
        os.makedirs(carpeta_salida)
        print(f"Carpeta '{carpeta_salida}' creada exitosamente.")

    for numero in numeros_archivos:
        nombre_archivo = f"texto_ficticio_{numero}.json"
        ruta_archivo = f"{directorio_actual}/textos/ejemplos/{nombre_archivo}"
        archivo_salida = f"{carpeta_salida}/texto-{numero}.json"
        
        # Validar la existencia del archivo antes de continuar
        if not os.path.exists(ruta_archivo):
            print(f"El archivo {ruta_archivo} no existe. Continuando con el siguiente.")
            continue
        
        # Enviar la solicitud curl y procesar la respuesta
        enviar_solicitud_curl(ruta_curl, ruta_archivo, archivo_salida)

def enviar_solicitud_curl(ruta_curl, ruta_archivo, archivo_salida):
    # Ejecutar el comando curl y capturar la salida en una variable
    comando_curl = f'curl -X POST -H "Content-Type: application/json" -d @"{ruta_archivo}" {ruta_curl}'
    salida_curl = subprocess.run(comando_curl, capture_output=True, text=True, shell=True).stdout
    
    print(comando_curl)
    
    # Escribir la salida capturada en un archivo JSON
    with open(archivo_salida, 'w') as archivo_json:
        archivo_json.write(salida_curl)
        print(f"Archivo {archivo_salida} creado exitosamente.")
      
    # Decodificar el texto escapado
    decodificar_texto_escapado(archivo_salida, archivo_salida)

if __name__ == "__main__":
    ruta_servicio_curl = "http://127.0.0.1:5000/extraer_entidades"  # Reemplaza con la URL de tu servicio
    
    numeros_archivos = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    procesar_archivos_seleccionados(ruta_servicio_curl, numeros_archivos)
