from flask import Blueprint
from sports_streaming.games.baseball.controller import api as baseball_api


api = Blueprint('sports_streaming', __name__, url_prefix='/api') # app level blueprint


# blueprint modules
api.register_blueprint(baseball_api)
