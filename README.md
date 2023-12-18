# API-ExtraccionDeEntidades

Proyecto de API para extraccion de entidades de un bloque de texto plano

INSTALAR PARA CORRER LA API
python.exe -m pip install --upgrade pip
pip install spacy
python -m spacy download es_core_news_sm
pip install Flask

COMPLETAR EL ARCHIVO DE MANERA AUTOMATICA
pip freeze > requirements.txt

INSTALAR LAS DEPENDENCIAS NECESARIAS
pip install -r requirements.txt

CORRER API
python app/main.py

CURL MUESTRA
CURL 1:
curl -X POST -H "Content-Type: application/json" -d "{\"texto\":\"El cliente realizó un pago de $500 con la tarjeta de crédito 1234-5678-9012-3456. La cuenta bancaria asociada es 9876-5432-1098-7654.\"}" http://127.0.0.1:5000/extraer_entidades > entidadesCapturadas.json

CURL 2:
curl -X POST -H "Content-Type: application/json" -d "{\"texto\":\"CAUSA Nº 3885-M CCALP FISCO DE LA PROVINCIA DE BUENOS AIRES C/ HIJOS DE JUAN CARLOS PEREZ S.A. Y OTROS S/ APREMIO PROVINCIAL. En la ciudad de La Plata, 5487-4589-5478-5214 a los dieciséis días del mes de agosto del año dos mil siete, reunida la Cámara de Apelación en lo Contencioso Administrativo con asiento en La Plata, en Acuerdo Ordinario, para pronunciar sentencia en la causa 'FISCO DE LA PROVINCIA DE BUENOS AIRES C/ HIJOS DE JUAN CARLOS PEREZ S.A. Y OTROS S/ APREMIO PROVINCIAL , en trámite ante el Juzgado de Primera Instancia en lo Contencioso Administrativo Nº 1 del Departamento Judicial de Bahía Blanca (expte. Nº -1878-), con arreglo al sorteo de ley, deberá observarse el siguiente orden de votación: Señores Jueces Dres. Gustavo Juan De Santis, Gustavo Daniel Spacarotel y Claudia Angélica Matilde Milanta. El Tribunal resolvió plantear la siguiente: C U E S T I Ó N: ¿Es justo el pronunciamiento apelado? A la cuestión planteada, el Dr. De Santis dijo: 1. Vienen los autos a esta instancia de apelación en razón del recurso articulado por la demandada, a fojas 103/108, contra la decisión del juez de la causa dictada a fojas 91/95. Por ese pronunciamiento, el a-quo rechaza las excepciones de falta de legitimación pasiva, inhabilidad de título y prescripción, opuestas por la accionada al progreso de la ejecución por la que el Estado Provincial persigue de ella el cobro de los créditos fiscales de los que da cuenta el título ejecutivo número 122.077, agregado a fojas 8/10. El Tribunal resolvió plantear la siguiente CUESTION: ¿Es admisible, y en su caso, fundado el recurso de apelación interpuesto? VOTACION: A la cuestión planteada, el Dr. Spacarotel dijo: I. La parte actora deduce recurso de apelación contra el pronunciamiento de grado que manda a llevar adelante la ejecución por un monto de capital inferior al que resulta del título ejecutivo base del proceso de apremio, declara la inconstitucionalidad de los artículos 96 y 104 del Código Fiscal (texto conf. ley 14.394) y en consecuencia, determina que los intereses sobre ese importe de capital se aplicarán conforme a la tasa activa vigente del Banco de la Provincia de Buenos Aires computándose a partir de la mora producida en cada período de vencimiento y hasta su efectivo pago. II. Apela a fs. 60/64, fundándolo en el mismo escrito de interposición. III.1. El recurso ha sido interpuesto en término y resulta admisible, toda vez que se agravia de la sentencia de trance y remate, que según alega causa un gravamen irreparable (arts. 244, CPCC; 10 y 18, dec. ley 9122/78 –13 y 25, ley 13.406-). Es doctrina de este Tribunal que el principio de apelación limitada, propio del proceso de apremio admite por vía de excepción, la recurribilidad de las resoluciones que generen un gravamen de difícil reparación ulterior (arts. 8, 10 y 18, dec. ley 9122/78; doc. CCALP, causa Nº 345 'Fisco de la Provincia de Buenos Aires C/ Juliani Cándida Delia S/ Apremio Provincial. Recurso de Queja', res. del 11-11-04 y sus citas). En el caso de autos, los agravios contenidos en la apelación encuadran dentro de la aludida salvedad, toda vez que del desdoblamiento de oficio del monto del título ejecutivo, cuando éste reúne las formas exigibles, implica en sí mismo un gravamen irreparable (doc. CCALP, causa Nº 532 'Fisco de la Provincia de Buenos Aires C/ Sabella y otros S/ Apremio Provincial', res. del 16-12-04). A ello debe agregarse, la declaración de inconstitucionalidad que formula el iudex en el pronunciamiento apelado, fundamenta el agravio y despeja toda duda sobre su recurribilidad. Máxime cuando, en la actualidad, la redacción del art. 13 de la ley 13.406 –de Apremios- expresamente prescribe la posibilidad que la actora recurra aquellas sentencias que no acogieran, en forma íntegra, la pretensión. Corresponde, en consecuencia, considerar los fundamentos de la impugnación interpuesta.\"}" http://127.0.0.1:5000/extraer_entidades > entidadesCapturadas.json
