from flask import jsonify
from werkzeug.exceptions import NotFound, InternalServerError, BadRequest, Forbidden, Unauthorized, MethodNotAllowed, ServiceUnavailable, RequestTimeout, TooManyRequests, BadGateway

# Manejo del error 404 - No encontrado
def manejo_not_found_error(e):
    return jsonify(error=str(e)), 404

# Manejo del error 500 - Error interno del servidor
def manejo_internal_server_error(e):
    return jsonify(error=str(e)), 500

# Manejo del error 400 - Solicitud incorrecta
def manejo_bad_request_error(e):
    return jsonify(error=str(e)), 400

# Manejo del error 403 - Prohibido
def manejo_forbidden_error(e):
    return jsonify(error=str(e)), 403

# Manejo del error 401 - No autorizado
def manejo_unauthorized_error(e):
    return jsonify(error=str(e)), 401

# Manejo del error 405 - Método no permitido
def manejo_method_not_allowed_error(e):
    return jsonify(error=str(e)), 405

# Manejo del error 503 - Servicio no disponible
def manejo_service_unavailable_error(e):
    return jsonify(error=str(e)), 503

# Manejo del error 408 - Tiempo de espera de la solicitud
def manejo_request_timeout_error(e):
    return jsonify(error=str(e)), 408

# Manejo del error 429 - Demasiadas solicitudes
def manejo_too_many_requests_error(e):
    return jsonify(error=str(e)), 429

# Manejo del error 502 - Puerta de enlace incorrecta
def manejo_bad_gateway_error(e):
    return jsonify(error=str(e)), 502
