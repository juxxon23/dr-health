from flask import Flask
from db.postgresql.model import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/dr-health'
    with app.app_context():
        db.init_app(app)
        db.create_all()
    return app
