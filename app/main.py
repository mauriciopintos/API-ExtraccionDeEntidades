# main.py
from flask import Flask, request, jsonify
import spacy
from spacy.tokens import Doc
from spacy.language import Language
from modules.spacy_component_module import load_spacy_components
from modules.regex_module import extract_domicilios

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

    # Procesar el texto con regex
    domicilios = patron_domicilio.findall(texto)

    # Identificar nombres propios
    nombres_propios = [ent.text for ent in doc.ents if ent.label_ == "PER"]

    resultado = {**doc._.datos_match, 'domicilio': domicilios, 'nombres_propios': nombres_propios}

    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)