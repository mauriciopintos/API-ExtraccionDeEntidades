from flask import Flask, request, jsonify
import spacy
import re

app = Flask(__name__)
nlp = spacy.load('es_core_news_sm')

@app.route('/extraer_entidades', methods=['POST'])
def extraer_entidades():
    datos = request.get_json()
    texto = datos.get('texto', '')

    # Procesar el texto con spaCy
    doc = nlp(texto)

    # Definir patrones de regex para datos sensibles
    regex_tarjeta = re.compile(r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b')
    regex_cuenta_bancaria = re.compile(r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b')
    regex_telefono = re.compile(r'\b(?:\+\d{1,2}\s?)?(\d{3,4}[ -]?)?\d{8,}\b')
    regex_domicilio = re.compile(r'\b\d+\s+[a-zA-Z]+\s+\w+\b')

    # Extraer nombres de personas, domicilios y localidades
    nombres_personas = [entidad.text for entidad in doc.ents if entidad.label_ == 'PER']
    domicilios = regex_domicilio.findall(texto)
    localidades = [entidad.text for entidad in doc.ents if entidad.label_ == 'LOC']

    # Agregar más patrones según sea necesario

    # Extraer entidades y datos sensibles
    entidades = [{'texto': entidad.text, 'tipo': entidad.label_} for entidad in doc.ents]

    datos_sensibles = {
        'tarjetas_credito': regex_tarjeta.findall(texto),
        'cuentas_bancarias': regex_cuenta_bancaria.findall(texto),
        'telefonos': regex_telefono.findall(texto),
        'domicilios': domicilios,
        'nombres_personas': nombres_personas,
        'localidades': localidades,
        # Agregar más campos según sea necesario
    }

    resultado = {'entidades': entidades, 'datos_sensibles': datos_sensibles}

    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)
