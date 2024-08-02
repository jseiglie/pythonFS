from flask import Flask
from api.config.config import Config
from api.models.models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
        
    return app