import os
from flask import Flask, Blueprint, request


bp = Blueprint("market", __name__)

from app import routes

def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(bp)
    
    return app

