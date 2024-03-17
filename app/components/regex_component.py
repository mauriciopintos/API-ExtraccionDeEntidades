# regex_component.py
import re

def extract_domicilios():
    # Patrón regex para extraer domicilios (tu patrón aquí)
    patron_domicilio = re.compile(r'\b(?:Ruta|Calle|Avenida|Av\.|Cra\.|Carrera|Pasaje|Pje\.|Plaza|Pza\.|Plz\.|Camino|Cd\.|Col\.|Colonia|Barrio)\s+[^\d,]+(?:\d{1,5}(?:[^\d,]+[^\d,]*)*)*\b')
    return patron_domicilio
