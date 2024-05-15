from flask import Flask, jsonify, render_template
from random import choice
import os

app = Flask(__name__)


pokeneas = [
    {"id": 1, "nombre": "Pikachu", "altura": 0.4, "habilidad": "Electricidad", "imagen": "https://storage.googleapis.com/pokenea-1/pikashu.png", "frase_filosofica": "A pesar de todo sigo de pie"},
    {"id": 2, "nombre": "Bulbasaur", "altura": 0.7, "habilidad": "Hierba", "imagen": "https://storage.googleapis.com/pokenea-1/bulbasaurio.png", "frase_filosofica": "whigga"},
    {"id": 3, "nombre": "Charmander", "altura": 0.6, "habilidad": "Fuego", "imagen": "https://storage.googleapis.com/pokenea-1/cristinini.png", "frase_filosofica": "ya no mas morbojoooooooooon"},
    {"id": 4, "nombre": "Squirtle", "altura": 0.5, "habilidad": "Agua", "imagen": "https://storage.googleapis.com/pokenea-1/cojone.png", "frase_filosofica": "how can i be gae, mi bitch is homophobic"},
    {"id": 5, "nombre": "Jigglypuff", "altura": 0.5, "habilidad": "Canto", "imagen": "https://storage.googleapis.com/pokenea-1/jiggly.png", "frase_filosofica": "peruan depresion"},
    {"id": 6, "nombre": "Eevee", "altura": 0.3, "habilidad": "Evolución", "imagen": "https://storage.googleapis.com/pokenea-1/perro.png", "frase_filosofica": "yo kreo que los fans de messi y cristiano deberiamos dejar de compararlos y besarnos entre todos"},
    {"id": 7, "nombre": "Snorlax", "altura": 2.1, "habilidad": "Dormir", "imagen": "https://storage.googleapis.com/pokenea-1/drome.png", "frase_filosofica": "small dick, big feelings"}
]

@app.route('/')
def json_pokenea():
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)