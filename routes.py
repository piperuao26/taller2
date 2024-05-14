from flask import Blueprint, jsonify, render_template
from random import choice
import os

pokeneas_bp = Blueprint('pokeneas_bp', __name__)

@pokeneas_bp.route('/')
def json_pokenea():
    from app import pokeneas
    container_id = os.uname()[1]
    pokenea = choice(pokeneas)
    data = {
        "id": pokenea["id"],
        "nombre": pokenea["nombre"],
        "altura": pokenea["altura"],
        "habilidad": pokenea["habilidad"],
        "id_contenedor": container_id  # Aquí puedes obtener el id del contenedor de alguna forma
    }
    return jsonify(data)

@pokeneas_bp.route('/foto_pokenea')
def foto_pokenea():
    from app import pokeneas
    pokenea = choice(pokeneas)
    container_id = os.uname()[1]
    return render_template('foto_pokenea.html', pokenea=pokenea, container_id=container_id)
