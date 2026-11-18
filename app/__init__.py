import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    # Secret key required to encrypt session cookies (storing OAuth token state)
    app.secret_key = os.getenv("FLASK_SECRET_KEY", "dev-key-change-in-production")
    
    from app.routes import main_bp
    app.register_blueprint(main_bp)
    
    return app
