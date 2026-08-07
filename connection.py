from dotenv import load_dotenv
import os

from flask_sqlalchemy import SQLAlchemy

load_dotenv()
db = SQLAlchemy()


class Config:
    SQLALCHEMY_DATABASE_URI=os.getenv('URL_DATABASE')

    # desabilitar o rastreamento de modificação dos objetos
    SQLALCHEMY_TRACK_MODIFICATIONS = False
