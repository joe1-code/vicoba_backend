from flask import Flask
from flask_migrate import Migrate
from .extensions import db
from .commands import create_tables
# from .routes import main

def create_app(config_file='settings.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    db.init_app(app)
    migrate = Migrate(app, db)

    # # Routes for module ...
    # app.register_blueprint(main)

    app.cli.add_command(create_tables)
    print('yoooo<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')

    return app
