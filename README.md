# Proyecto: API-ExtraccionDeEntidadesNombradas (API-EDEN)

La presente API, esta desarrollada con el objetivo de extraer entidades nombradas especificas de un texto en lenguaje natural.

## Índice

- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Endpoints](#endpoints)
- [Ejemplos](#ejemplos)
- [Base conceptual](#base-conceptual)

## Instalación

Para que la API funcione correctamente, es necesario instalar los paquetes y todos los componentes necesarios

```bash
python.exe -m pip install --upgrade pip
pip install -U pip setuptools wheel
pip install -U spacy
python -m spacy download es_core_news_lg
pip install Flask
pip install openai
pip install openai==0.28
pip freeze > requirements.txt
pip install -r requirements.txt
pip install beautifulsoup4
```

## USO

Para correr la API de manera manual, es necesario ejecutar en la terminal, desde el path donde se encuentra la carpeta "app" el archivo "main.py" de la siguiente manera:

```bash
python app/main.py
```

## Estructura del Proyecto

```bash
|-- API-EDEN/
|   |-- app/
|   |   |-- main.py
|   |   |-- components/
|   |   |   |-- __init__.py
|   |   |   |-- OpenAI_component.py
|   |   |   |-- regex_component.py
|   |   |   |-- spacy_component.py
|   |   |   |-- tools/
|   |   |   |   |-- decode_escapado.py
|   |   |   |   |-- verifica_OpenAI_config.py
|   |   |-- models/
|   |   |   |-- __init__.py
|   |-- config/
|   |   |-- __init__.py
|   |   |-- OpenAI_config.json
|   |   |-- TEMPLATE_OpenAI_config.json
|   |-- tests/
|   |   |-- decode_escapado_test.py
|   |   |-- test_extraccion_entidades_GPT.py
|   |   |-- textos/
|   |   |   |-- ejemplos/
|   |   |   |-- entidades/
|   |-- .gitignore
|   |-- README.md
|   |-- requirements.txt
```

## Endpoints

Actualmente, la API solo cuenta con un endpoint, pero a medida que se avance con el proyecto se podran incorporar otros de ser necesario.

`/api/extraer_entidades`

- Método: POST
- Descripción: Extrae entidades en formato JSON.
- Parámetros: curl -X POST -H "Content-Type: application/json" -d "{\"texto\":\"Hola, mundo.\"}" http://127.0.0.1:5000/extraer_entidades

## Ejemplos

Una vez que la API se encuentra corriendo, podemos probarla mediante CURL desde la consola CMD en Windows o Terminal de Linux, como se muestra en los ejemplos.

- Ejemplos CURL

CURL 1:

```bash
curl -X POST -H "Content-Type: application/json" -d "{\"texto\":\"Hola, mi nombre es Juan Pérez y vivo en la Calle Falsa 123, Buenos Aires. Mi DNI es 12.345.678 y mi teléfono es 11-2345-6789. También tengo un segundo DNI, el 87.654.321. Puedes contactarme a mi correo electrónico juan.perez@mail.com o a mi teléfono alternativo (11) 4 567-8901. Mi hermana, María Pérez, vive en Avenida Siempreviva 456, Rosario. Su DNI es 98.765.432 y su teléfono es 341-2345-678. Su correo electrónico es maria.perez@mail.com. Recientemente, compré un auto con la patente ABC123 y mi hermana compró uno con la patente DE456FG. Mi tarjeta de crédito es 1234 5678 9012 3456 y la de mi hermana es 7890-1234-5678-9012. Mi número de cuenta es 1234567-8 y el de mi hermana es 8765432/1. Por favor, no compartas esta información con nadie ya que son datos sensibles. Gracias. \"}" http://127.0.0.1:5000/extraer_entidades
```

CURL 2:

```bash
curl -X POST -H "Content-Type: application/json" -d "{\"texto\":\"Hola, mi nombre es Juan Pérez y vivo en la Calle Falsa 123, Buenos Aires. Mi DNI es 12.345.678 y mi teléfono es 11-2345-6789. También tengo un segundo DNI, el 87.654.321. Puedes contactarme a mi correo electrónico juan.perez@mail.com o a mi teléfono alternativo (11) 4 567-8901. Mi hermana, María Pérez, vive en Avenida Siempreviva 456, Rosario. Su DNI es 98.765.432 y su teléfono es 341-2345-678. Su correo electrónico es maria.perez@mail.com. Recientemente, compré un auto con la patente ABC123 y mi hermana compró uno con la patente DE456FG. Mi tarjeta de crédito es 1234 5678 9012 3456 y la de mi hermana es 7890-1234-5678-9012. Mi número de cuenta es 1234567-8 y el de mi hermana es 8765432/1. Por favor, no compartas esta información con nadie ya que son datos sensibles. Gracias. En la mágica Avenida de los Sueños, donde las Calles se entrelazan como historias encantadas, vivía Juan Pérez, el guardián del Pasaje de las Maravillas. Su DNI, con el número dd ddd ddd, era un secreto celosamente protegido. El Teléfono misterioso, 11-2345-6789, resonaba como un encantamiento en la Plaza de los Misterios. María Pérez, la exploradora de la Colonia de las Mariposas, poseía una Tarjeta con el código mágico: 7890-1234-5678-9012. Su Cuenta, marcada como ddddddd/d, era un tesoro escondido en la Calle de los Tesoros. El Correo electrónico, maria.perez@mail.com, era una puerta a su mundo secreto. En el Camino de los Deseos, los coches exhibían Patentes únicas. Juan manejaba el XXdddXX, mientras que María conducía el XXXddd. Las letras y números en sus autos eran como un lenguaje codificado en el Cruce de las Letras. En el Barrio de los Misterios, las historias se tejían con las Tarjetas de Crédito, y los números 1234 5678 9012 3456 eran la clave de acceso a la Galería de los Tesoros. La Avenida de los Secretos albergaba el misterioso Correo electrónico, juan.perez@mail.com, una dirección exclusiva conocida solo por unos pocos. Estas entidades se entrelazaban en una danza encantada en la Carrera de las Estrellas, donde los números y las letras cobraban vida en cada Esquina. En la Colonia de los Sueños, la magia de los DNI, Teléfonos, Correos electrónicos, Tarjetas, Cuentas y Patentes creaba un tejido místico que solo aquellos con ojos curiosos podían descifrar. Generar un texto de ficción con un número específico de entidades puede ser un desafío, ya que la generación de texto es un proceso creativo y no hay garantía de que se obtendrán un número exacto de entidades en cada categoría. Sin embargo, puedo proporcionarte un texto ficticio que incluye múltiples instancias de las entidades que has especificado, tratando de cumplir con tus requisitos. Había una vez en la bulliciosa Calle del Sol, donde las Avenidas entrelazaban historias y los Pasajes susurraban secretos. En este vibrante Barrio, las vidas se entrecruzaban como los caminos de una Colonia en constante movimiento. Juan Pérez, dueño de la Tarjeta dorada con números mágicos, caminaba por la Plaza central. Su DNI, guardado en el bolsillo con formato dd ddd ddd, era un misterio para los curiosos. La multitud en el Pje. de las Mariposas se emocionaba al escuchar su número de Teléfono, 11-2345-6789, una melodía única en la Ciudad.Mientras tanto, en el rincón tranquilo de la Calle de las Sombras, María Pérez guardaba celosamente su Correo electrónico, maria.perez@mail.com. Su Cuenta secreta, marcada como dddddd-d, era un enigma para los vecinos curiosos. El misterioso Patrón de su coche, XXdddXX, dejaba una huella intrigante en cada esquina de la Av. de los Sueños.\"}" http://127.0.0.1:5000/extraer_entidades
```

## Base conceptual

https://docs.python.org/es/3/library/re.html#
https://regex101.com/
https://spacy.io/usage
https://spacy.io/api
https://www.textraction.ai/
https://oa.upm.es/
https://github.com/IBacieroFdez/SpanishNER/blob/master/Code/.ipynb_checkpoints/patterns-checkpoint.ipynb
https://pro.arcgis.com/es/pro-app/3.0/tool-reference/geoai/train-entity-recognition-model.htm
https://platform.openai.com/docs/introduction
https://platform.openai.com/docs/assistants/overview?context=with-streaming
https://learn.microsoft.com/es-es/azure/ai-services/openai/
https://learn.microsoft.com/es-es/azure/ai-services/openai/api-version-deprecation
