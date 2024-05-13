from flask import Blueprint, jsonify, render_template
from random import choice


pokeneas_bp = Blueprint('pokeneas_bp', __name__)

@pokeneas_bp.route('/json_pokenea')
def json_pokenea():
    from app import pokeneas
    pokenea = choice(pokeneas)
    data = {
        "id": pokenea["id"],
        "nombre": pokenea["nombre"],
        "altura": pokenea["altura"],
        "habilidad": pokenea["habilidad"],
        "id_contenedor": "id_del_contenedor"  # Aquí puedes obtener el id del contenedor de alguna forma
    }
    return jsonify(data)

@pokeneas_bp.route('/foto_pokenea')
def foto_pokenea():
    from app import pokeneas
    pokenea = choice(pokeneas)
    return render_template('foto_pokenea.html', pokenea=pokenea)
