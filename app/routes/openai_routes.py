# openai_routes.py
from flask import Blueprint, jsonify
from components.tools.valida_openai_config import validar_config

openai_blueprint = Blueprint('openai', __name__)

@openai_blueprint.route('/valida_openai_config', methods=['GET'])
def valida_openai_config():
    try:
        validar_config()
        return jsonify({"message": "Las credenciales de OpenAI son correctas."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
