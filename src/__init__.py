from flask import Flask
from connection import db, Config, ma
from flask_marshmallow import Marshmallow


ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    ma.init_app(app) 


    # opcional para verificar funcionamento do servidor
    @app.get('/')
    def home():
        return {"mensagem":"API Flask funcionando"}, 200

    return app