"""
Flask application instance

This is the entry point of the application. Here an instance of Flask is initialized.
Flask uses the location of the module passed here through `__name__` argument as a starting point when it needs
to load associated resources such as template files.

The second `import` is done at the bottom to avoid the so called circular dependency between modules. `routes` requires
the `app` variable, which is assigned the `Flask` instance.

Points of interest:
    - Circular imports
    - `__name__` argument
"""
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
