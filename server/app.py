# server/app.py
#!/usr/bin/env python3

from flask import Flask, jsonify
from flask_migrate import Migrate
from models import db, Pet

# Initialize app
app = Flask(__name__)

# Database config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)

# Example route
@app.route("/")
def index():
    return jsonify({"message": "Welcome to the Pet API!"})

@app.route("/pets")
def get_pets():
    pets = Pet.query.all()
    pets_list = [{"id": p.id, "name": p.name, "species": p.species} for p in pets]
    return jsonify(pets_list)

if __name__ == "__main__":
    app.run(port=5555, debug=True)
