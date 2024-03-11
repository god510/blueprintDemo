# __init__.py
from flask import Flask
from blueprints.home import home_blueprint
from blueprints.admin import admin_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_blueprint)
    app.register_blueprint(admin_blueprint, url_prefix='/admin')
    return app