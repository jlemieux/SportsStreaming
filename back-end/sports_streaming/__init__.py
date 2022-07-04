# from flask import Flask
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

from flask import Flask
from flask_cors import CORS
import config


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    CORS(app)

    from sports_streaming.api import api as api_blueprint
    app.register_blueprint(api_blueprint)

    return app


# from myapp.models.user import User  # noqa
# from myapp.models.message import Message  # noqa
# from myapp import api  # noqa