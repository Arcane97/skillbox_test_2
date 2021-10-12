from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
db = SQLAlchemy()
migrate = Migrate(app, db)


def create_app():
    app.config.from_pyfile('settings.py')
    db.init_app(app)

    from cats_shop.cats.routes import cats

    app.register_blueprint(cats)

    return app
