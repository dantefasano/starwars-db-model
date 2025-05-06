from flask import Flask, request, jsonify
from flask_cors import CORS
from src.models import db, User, Character, Planet, Favorite

app = Flask(__name__)
CORS(app)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Endpoints para Usuarios
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.serialize() for user in users])

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(user.serialize())

# Endpoints para Personajes
@app.route('/characters', methods=['GET'])
def get_characters():
    characters = Character.query.all()
    return jsonify([character.serialize() for character in characters])

@app.route('/characters/<int:character_id>', methods=['GET'])
def get_character(character_id):
    character = Character.query.get_or_404(character_id)
    return jsonify(character.serialize())

# Endpoints para Planetas
@app.route('/planets', methods=['GET'])
def get_planets():
    planets = Planet.query.all()
    return jsonify([planet.serialize() for planet in planets])

@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):
    planet = Planet.query.get_or_404(planet_id)
    return jsonify(planet.serialize())

# Endpoints para Favoritos
@app.route('/favorites', methods=['GET'])
def get_favorites():
    favorites = Favorite.query.all()
    return jsonify([favorite.serialize() for favorite in favorites])

@app.route('/favorites', methods=['POST'])
def create_favorite():
    data = request.get_json()
    favorite = Favorite(
        user_id=data['user_id'],
        character_id=data.get('character_id'),
        planet_id=data.get('planet_id')
    )
    db.session.add(favorite)
    db.session.commit()
    return jsonify(favorite.serialize()), 201

if __name__ == '__main__':
    app.run(debug=True) 