# spacy_component_module.py
import spacy
from spacy.tokens import Doc
from spacy.language import Language
from spacy.matcher import Matcher

def load_spacy_components():
    # Cargar el modelo de lenguaje
    nlp = spacy.load("es_core_news_lg")

    # Inicializar el matcher con el vocabulario compartido
    matcher = Matcher(nlp.vocab)

    # Definir patrones de Matcher
    patrones_match = {
        "DNI": [[{"SHAPE": "dd.ddd.ddd"}], [{"SHAPE": "dddddddd"}], [{"SHAPE": "dd ddd ddd"}]],
        "Telefono": [[{"SHAPE": "dd-dddd-dddd"}], [{"SHAPE": "dddd-dddd"}], [{"SHAPE": "dd dddd-dddd"}], [{"SHAPE": "(dd) d dd-dddd-dddd"}], [{"SHAPE": "(dd) d dd dddd-dddd"}], [{"SHAPE": "ddd-dddd-dddd"}], [{"SHAPE": "dddd-dddd-ddddd"}]],
        "Correo": [[{"LIKE_EMAIL": True}]],
        "Tarjeta": [[{"SHAPE": "dddd dddd dddd dddd"}], [{"SHAPE": "dddd-dddd-dddd-dddd"}], [{"SHAPE": "dddd - dddd - dddd - dddd"}]],
        "Cuenta": [[{"SHAPE": "ddddddd-d"}], [{"SHAPE": "ddddddd/d"}]],
        "Patente": [[{"SHAPE": "XXX-ddd"}], [{"SHAPE": "XXXddd"}], [{"SHAPE": "XXX ddd"}], [{"SHAPE": "XX-ddd-XX"}], [{"SHAPE": "XX ddd XX"}], [{"SHAPE": "XXdddXX"}]]
    }

    # Añadir patrones al matcher
    for label, patterns in patrones_match.items():
        for pattern in patterns:
            matcher.add(label, [pattern])

    # Registrar la extensión en el Doc
    if not Doc.has_extension("datos_match"):
        Doc.set_extension("datos_match", default=[])

    # Registrar el componente personalizado
    @Language.component("componente_match")
    def componente_match(doc):
        # Procesar el texto con matcher
        matches = matcher(doc)

        # Extraer entidades y datos sensibles
        datos_match = {}
        for match_id, start, end in matches:
            tipo_entidad = nlp.vocab.strings[match_id]
            texto_entidad = doc[start:end].text
            datos_match.setdefault(tipo_entidad, []).append(texto_entidad)

        # Añadir los datos sensibles al doc
        doc._.datos_match = datos_match

        return doc

    # Añadir el componente personalizado al pipeline
    nlp.add_pipe("componente_match")

    return nlp, matcher
