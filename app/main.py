# main.py
from flask import Flask
from routes.extraccion_entidades_routes import entidades_blueprint
from routes.manejador_excepciones_routes import *
from routes.openai_routes import openai_blueprint

app = Flask(__name__)
app.register_blueprint(entidades_blueprint)
app.register_blueprint(openai_blueprint)


# Registrar los manejadores de errores
app.register_error_handler(NotFound, manejo_not_found_error)
app.register_error_handler(InternalServerError, manejo_internal_server_error)
app.register_error_handler(BadRequest, manejo_bad_request_error)
app.register_error_handler(Forbidden, manejo_forbidden_error)
app.register_error_handler(Unauthorized, manejo_unauthorized_error)
app.register_error_handler(MethodNotAllowed, manejo_method_not_allowed_error)
app.register_error_handler(ServiceUnavailable, manejo_service_unavailable_error)
app.register_error_handler(RequestTimeout, manejo_request_timeout_error)
app.register_error_handler(TooManyRequests, manejo_too_many_requests_error)
app.register_error_handler(BadGateway, manejo_bad_gateway_error)

if __name__ == '__main__':
    app.run(debug=True)
