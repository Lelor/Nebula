from flask import Flask

from server.config import get_config
from server.controllers.sign_up import bp as sign_up_bp
from server.database.model import db
from server.encoder import Encoder


def create_app():
    app = Flask(__name__)
    app.config.from_object(get_config())
    app.json_encoder = Encoder

    # registering blueprints.
    app.register_blueprint(sign_up_bp)

    # Initializing database.
    db.init_app(app)

    return app
