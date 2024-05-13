from flask import Flask
from routes import pokeneas_bp


app = Flask(__name__, template_folder='taller2/templates')
app.register_blueprint(pokeneas_bp)

pokeneas = [
    {"id": 1, "nombre": "Pikachu", "altura": 0.4, "habilidad": "Electricidad", "imagen": "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/detail/025.png", "frase_filosofica": "A pesar de todo sigo de pie"},
    {"id": 2, "nombre": "Bulbasaur", "altura": 0.7, "habilidad": "Hierba", "imagen": "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/001.png", "frase_filosofica": "whigga"},
    {"id": 3, "nombre": "Charmander", "altura": 0.6, "habilidad": "Fuego", "imagen": "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/detail/004.png", "frase_filosofica": "ya no mas morbojoooooooooon"},
    {"id": 4, "nombre": "Squirtle", "altura": 0.5, "habilidad": "Agua", "imagen": "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/detail/007.png", "frase_filosofica": "how can i be gae, mi bitch is homophobic"},
    {"id": 5, "nombre": "Jigglypuff", "altura": 0.5, "habilidad": "Canto", "imagen": "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/detail/039.png", "frase_filosofica": "peruan depresion"},
    {"id": 6, "nombre": "Eevee", "altura": 0.3, "habilidad": "Evolución", "imagen": "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/detail/133.png", "frase_filosofica": "yo kreo que los fans de messi y cristiano deberiamos dejar de compararlos y besarnos entre todos"},
    {"id": 7, "nombre": "Snorlax", "altura": 2.1, "habilidad": "Dormir", "imagen": "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/detail/143.png", "frase_filosofica": "small dick, big feelings"}
]

if __name__ == '__main__':
    app.run(debug=True)
