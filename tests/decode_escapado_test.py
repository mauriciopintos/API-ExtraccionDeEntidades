#    texto_decodificado = resultado.encode('utf-8').decode('unicode-escape')

def decodificar_texto_escapado(entrada, salida):
    with open(entrada, 'r', encoding='utf-8') as archivo_entrada:
        contenido = archivo_entrada.read()
        contenido_decodificado = contenido.encode('utf-8').decode('unicode-escape')

    with open(salida, 'w', encoding='utf-8') as archivo_salida:
        archivo_salida.write(contenido_decodificado)
