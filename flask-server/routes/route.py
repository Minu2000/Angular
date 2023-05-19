from flask import Flask, jsonify, request,Blueprint
from services.service import Service
from services.service import search_product
from flask_jwt_extended import jwt_required,get_jwt_identity

ab = Blueprint('api', __name__)
service_instance = Service()

@ab.route('/api/v1/register', methods=['POST'])
def register():
    try:
        return service_instance.register()
    except Exception as e:
        return jsonify({"error":str(e)})


@ab.route('/api/v1/login', methods=['POST'])
def login():
    try:
        return service_instance.login()
    except Exception as e:
        return jsonify({"error":str(e)})


