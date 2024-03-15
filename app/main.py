# main.py
from flask import Flask, Response, request, jsonify
from components.spacy_component import load_spacy_components
from components.regex_component import extract_domicilios
from components.OpenAI_component import extraer_entidades_GPT

app = Flask(__name__)

# Carga el modelo de lenguaje y carga componentes de SpaCy
nlp, matcher = load_spacy_components()

# Patrón regex para extraer domicilios
patron_domicilio = extract_domicilios()

@app.route('/extraer_entidades', methods=['POST'])
def extraer_entidades():
    datos = request.get_json()
    texto = datos.get('texto', '')

    # Procesar el texto con spaCy
    doc = nlp(texto)

    # Procesar el texto con regex para extraer domicilios
    domicilios = patron_domicilio.findall(texto)

    # Identificar nombres propios
    nombres_propios = [ent.text for ent in doc.ents if ent.label_ == "PER"]

    # Crear el resultado con campos no nulos
    resultado = {
        key: value for key, value in {
            'Tarjeta': doc._.datos_match.get('Tarjeta'),
            'DNI': doc._.datos_match.get('DNI'),
            'Telefono': doc._.datos_match.get('Telefono'),
            'Correo': doc._.datos_match.get('Correo'),
            'Cuenta': doc._.datos_match.get('Cuenta'),
            'Patente': doc._.datos_match.get('Patente'),
            'nombres_propios': nombres_propios if nombres_propios else None,
            'domicilios': domicilios if domicilios else None
        }.items() if value is not None
    }
    
    
    # Eliminar duplicados de cada lista en el resultado
    for key in resultado.keys():
        if isinstance(resultado[key], list):
            resultado[key] = list(set(resultado[key]))

    #response_json = Response(data_json, mimetype='application/json')
    salida_gpt = extraer_entidades_GPT(resultado)
    
    # Devolver la salida formateada
    return salida_gpt

if __name__ == '__main__':
    app.run(debug=True)
