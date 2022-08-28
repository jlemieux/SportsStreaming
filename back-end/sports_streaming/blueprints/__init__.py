from flask import Blueprint
from sports_streaming.games.baseball.controller import api as baseball_api
from sports_streaming.games.football.controller import api as football_api


api = Blueprint('sports_streaming', __name__, url_prefix='/api') # app level blueprint


# blueprint modules
api.register_blueprint(baseball_api)
api.register_blueprint(football_api)
