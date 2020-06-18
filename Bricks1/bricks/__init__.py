from bricks.config import Config
from flask import Flask 
from peewee import *


db = SqliteDatabase('bricks/dados.db')


def create_app(config_class=Config):
  app = Flask(__name__)
  app.config.from_object(config_class)
  

  from bricks.lance import lance_bp
  app.register_blueprint(lance_bp)
  
  from bricks.index import index_bp
  app.register_blueprint(index_bp)

  from bricks.incluir_item import incluirItem_bp
  app.register_blueprint(incluirItem_bp)

  from bricks.home import home_bp
  app.register_blueprint(home_bp)


  return app




